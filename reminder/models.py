# -*- coding: utf-8 -*-
from django.db import models


class Proxy(models.Model):
    '''抓取的代理'''
    site = models.URLField('来源网址', max_length=100)
    ip = models.GenericIPAddressField('IP地址', unique=True)
    port = models.PositiveSmallIntegerField('端口')
    anonymity = models.CharField('匿名度:透明/匿名/高匿名', max_length=10)
    http = models.CharField('类型: HTTP/HTTPS', max_length=20)
    action = models.CharField('get/post支持', max_length=20)
    address = models.CharField('位置', max_length=50)
    created_at = models.DateTimeField('添加时间', auto_now_add=True)
