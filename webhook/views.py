# -*- coding: utf-8 -*-

import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


__author__ = 'haofly'
__datetime__ = '2016-06-03 16:40:00'
__description__ = 'github的webhook钩子'


@csrf_exempt
def webhook(request):
    os.system('cd /var/www/admin')
    os.system('git pull -f git@github.com:haoflynet/admin.git 2>&1')
    return HttpResponse('ok')
