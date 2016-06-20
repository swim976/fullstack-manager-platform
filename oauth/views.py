# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate

from .forms import LoginForm


def weblogin(request):
    '''登录功能'''
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            print('用户验证并登录成功')
            django_login(request, user)
        else:
            return JsonResponse({'code': 404, 'message': '用户认证事变'})

        return JsonResponse({'code': 200, 'message': 'ok'})
    else:
        return JsonResponse({'code': 403, 'message': '表单错误'})

'''如果是移动端嘛，那么accessToken的时候也会带上appkey和appsecret，当然还会带上用户名密码，
最后返回过去的就是一个token，这个token是与该用户关联的，就相当于web里的session
'''


def login(request):
    '''登录认证接口
    POST
    Args:
        client_id: AppKey
        client_secret: AppSecret
        user_name:
        password:

    Returns:
        json数据：
        code: 200
        session: 'ACCESS_TOKEN'
        expires_in: 1234,
        user_id:
    '''
    pass


def getTokenInfo(request):
    '''查询access_token的授权相关信息，包括授权时间，过期时间和scope权限
    POST
    Args:
        access_token: 'ACCESS_TOKEN'

    Returns:
        json数据:
        code: 200
        appkey: AppKey
        scope:
        create_at
        expire_in
    '''
    pass


def revokeOauth(request):
    '''授权回收接口
    POST
    Args:
        access_token: 'ACCESS_TOKEN'

    Returns:
        json数据:
        code: 200
        result: true
    '''
    pass
