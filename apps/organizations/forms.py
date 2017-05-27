# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/5/27 20:40'
from django import forms
from operation.models import UserAsk

# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     mobile = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, min_length=5, max_length=5)


class UserAskForm(forms.ModelForm):
    #当然了也可以在这里添加自己的字段
    #myField = forms.CharField()
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']