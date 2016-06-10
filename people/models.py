# -*- coding: utf-8 -*-
from django.db import models


SEX_CHOICES = (
    (1, '男'),
    (0, '女'),
)


class People(models.Model):
    '''人力资源'''
    name = models.CharField(max_length=10)
    birth_lunar = models.DateField(null=True, '农历生日')
    birth_new = modles.DateField(null=True, '新历生日')
    sex = SEX_CHOICES
    phone = models.IntegerField(null=True, '电话号码')
    qq = models.IntegerField(null=True, 'QQ')
    wechat(max_length=20, null=True, '微信号')
    school(max_length=15, null=True, '学校(逗号分隔)')
    old_address(max_length=30, null=True, '老家地址')
    present_address(max_length=30, null=True, '现居地')
    company(max_length=30, null=True, '公司')
    job(max_length=10, null=True, '职位')
    relation(max_length=10, null=True, '关系')
    beta(max_length=100, null=True, '备注')
