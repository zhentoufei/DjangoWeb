# -*- coding:utf-8 -*-
from django.shortcuts import render

from django.views.generic.base import View

from .models import Course, CourseResource
from operation.models import UserFavorite, CourseComment, UserCourse

from pure_pagination import Paginator, PageNotAnInteger
from django.http import HttpResponse
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by("-click_nums")[:3]
        # 课程排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        # 对课程机构分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 3, request=request)
        courses = p.page(page)

        return render(request, 'course-list.html', {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses
        })


class CourseDetailView(View):
    '''
    课程详情页面
    '''

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        # 增加课程点击数
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        tag = course.tag
        if tag:
            related_course = Course.objects.filter(tag=tag)[:1]
        else:
            related_course = []
        return render(request, "course-detail.html", {
            'course': course,
            'related_course': related_course,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org
        })


class CourseInfoView(LoginRequiredMixin, View):
    '''
    课程章节信息
    '''

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        #查询用户是否已经关联了该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()
        # 取出所有课程id
        course_ids = [user_course.course.id for user_course in user_courses]
        # 取出学过该用户学习过的其他的课程
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-video.html", {
            "course": course,
            "all_resources": all_resources,
            "relate_courses": relate_courses
        })


class CommentsView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComment.objects.all()
        return render(request, "course-comment.html", {
            "course": course,
            "all_resources": all_resources,
            "all_comments": all_comments
        })


class AddCommentsView(View):
    '''
    用戶添加課程評論
    '''

    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if course_id > 0 and comments:
            course_comment = CourseComment()
            course = Course.objects.get(id=int(course_id))
            course_comment.course = course
            course_comment.comment = comments
            course_comment.user = request.user
            course_comment.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:

            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')
