# -*- coding:utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/5/27 20:49'

from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView
urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),

    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),

    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name='course_comment'),

    url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comment'),

]