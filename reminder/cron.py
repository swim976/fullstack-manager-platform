# -*- coding: utf-8 -*-
import datetime
import re
import requests
from people.models import People
from django.db.models import Q
from . import service
__description__ = '各种定时任务'


def checkGithub():
    '''git提醒'''
    today = str(datetime.date.today())
    r = requests.get('https://github.com/haoflynet')
    match = re.search(
                'data-count="(?P<count>\d+)" data-date="' + today + '"',
                r.text)

    count = int(match.group('count'))    # 当天提交数

    if count == 0:
        service.sendGitCommitSMS('haofly', 'admin project')


def checkBirth():
    '''查询明天生日的人，百度查询，今天是农历几月几日'''
    old_month, old_day = service.getLunar()
    today = datetime.date.today()
    new_month, new_day = today.month, today.day

    # 提示最近七天的生日
    peoples = []
    for _i in range(7):
        peoples.append(People.objects.filter(
            (Q(birth_lunar__month=old_month) & Q(birth_lunar__day=old_day)) |
            (Q(birth_new__month=new_month) & Q(birth_new__day=new_day))
        ))
        old_month, old_day = service.getNextDate(old_month, old_day, 1)
        new_month, new_day = service.getNextDate(new_month, new_day, 1)
    email = service.generateBirthEmail(peoples)
    service.sendEmail(email, '定时任务-生日提醒')
