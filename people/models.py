# -*- coding: utf-8 -*-
from django.db import models


SEX_CHOICES = (
    (1, '男'),
    (0, '女'),
)


class People(models.Model):
    """
    人力资源
    """
    name = models.CharField('姓名', max_length=10)
    pinyin = models.CharField('拼音', max_length=50)
    birth_lunar = models.DateField('农历生日', null=True, blank=True)
    birth_new = models.DateField('新历生日', null=True, blank=True)
    familiar = models.SmallIntegerField('亲密度(0亲人/1朋友/2熟悉/3认识/4可能不认识我了/5陌生人)', null=True, blank=True)
    sex = models.SmallIntegerField('性别', null=True, choices=SEX_CHOICES, blank=True)
    phone = models.CharField('电话号码', max_length=12, null=True, blank=True)
    qq = models.CharField('QQ', max_length=12, null=True, blank=True)
    wechat = models.CharField('微信号', max_length=20, null=True, blank=True)
    school = models.CharField('学校(逗号分隔)', max_length=15, null=True, blank=True)
    old_address = models.CharField('老家地址', max_length=30, null=True, blank=True)
    present_address = models.CharField('现居地', max_length=30, null=True, blank=True)
    company = models.CharField('现居地', max_length=30, null=True, blank=True)
    job = models.CharField('职位', max_length=10, null=True, blank=True)
    relation = models.CharField('关系', max_length=10, null=True, blank=True)
    beta = models.CharField('备注', max_length=100, null=True, blank=True)
    id_card = models.CharField('证件号码', max_length=20, null=True, blank=True)
    car_num = models.CharField('车牌号', max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name
