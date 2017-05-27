# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/5/27 20:49'

from django.conf.urls import url, include
from .views import OrgView
urlpatterns = [
    #课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', OrgView.as_view(), name='org_list'),
]