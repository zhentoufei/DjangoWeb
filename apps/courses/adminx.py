# -*- coding: utf-8 -*-
import xadmin
from .models import Course, Lesson, Video, CourseResource
from organizations.models import CourseOrg

__author__ = 'Mr.Finger'
__date__ = '2017/5/2 20:47'


class Lessoninline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class BannerCourse(Course):
    class Meta:
        verbose_name = u'轮播课程'
        verbose_name_plural = verbose_name
        proxy = True


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times',
                     'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times',
                   'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    inlines = [Lessoninline, CourseResourceInline]
    ordering = ['-click_nums']  # 基于click_nums排序
    readonly_fields = ['click_nums']  # click_nums设置为只读
    exclude = ['fav_nums']  # 不显示fav_nums

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'students', 'fav_nums', 'image', 'click_nums', 'add_time', 'get_zj_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times',
                     'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times',
                   'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    inlines = [Lessoninline, CourseResourceInline]
    ordering = ['-click_nums']  # 基于click_nums排序
    readonly_fields = ['click_nums']  # click_nums设置为只读
    exclude = ['fav_nums']  # 不显示fav_nums
    list_editable = ['degree', 'desc']
    refresh_times = [3, 4, 5]  # 设置定时刷新的时间
    style_fields = {"detail": "ueditor"}#指明detail页面使用的是ueditor

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数目
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
