# -*- coding: utf-8 -*-
from django.db import models


SEX_CHOICES = (
    (1, '男'),
    (0, '女'),
)


class People(models.Model):
    '''人力资源'''
    name = models.CharField('姓名', max_length=10)
    birth_lunar = models.DateField('农历生日', null=True)
    birth_new = modles.DateField('新历生日', null=True)
    sex = models.SmallIntegerField('性别', null=True, choices=SEX_CHOICES)
    phone = models.IntegerField('电话号码', null=True)
    qq = models.IntegerField('QQ', null=True)
    wechat('微信号', max_length=20, null=True)
    school('学校(逗号分隔)', max_length=15, null=True)
    old_address('老家地址', max_length=30, null=True)
    present_address('现居地', max_length=30, null=True)
    company('现居地', max_length=30, null=True)
    job('职位', max_length=10, null=True)
    relation('关系', max_length=10, null=True)
    beta('备注', max_length=100, null=True)
