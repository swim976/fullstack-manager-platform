# -*- coding: utf-8 -*-
from wsgiref.util import FileWrapper

from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    '''每个文件都应该有一个hello world'''
    FileWrapper()
    return HttpResponse('Hello World!')
