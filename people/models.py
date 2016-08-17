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
    birth_new = models.DateField('新历生日', null=True)
    sex = models.SmallIntegerField('性别', null=True, choices=SEX_CHOICES)
    phone = models.CharField('电话号码', max_length=12, null=True)
    qq = models.CharField('QQ', max_length=12, null=True)
    wechat = models.CharField('微信号', max_length=20, null=True)
    school = models.CharField('学校(逗号分隔)', max_length=15, null=True)
    old_address = models.CharField('老家地址', max_length=30, null=True)
    present_address = models.CharField('现居地', max_length=30, null=True)
    company = models.CharField('现居地', max_length=30, null=True)
    job = models.CharField('职位', max_length=10, null=True)
    relation = models.CharField('关系', max_length=10, null=True)
    beta = models.CharField('备注', max_length=100, null=True)

    def __str__(self):
        return self.name
