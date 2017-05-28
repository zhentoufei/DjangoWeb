# -*- coding: utf-8 -*-
__author__ = 'Mr.Finger'
__date__ = '2017/5/27 20:40'
from django import forms
from operation.models import UserAsk
import re


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

    def clean_mobile(self):
        '''
        验证手机号码是否合法
        :return: 
        '''
        mobile = self.cleaned_data["mobile"]
        REGEX_MOBILE = R"^1(3[0-9]|4[57]|5[0-35-9]|7[0135678]|8[0-9])\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")