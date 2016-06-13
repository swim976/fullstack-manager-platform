# -*- coding: utf-8 -*-
import datetime
import re
import requests
from people.models import People
from django.db.models import Q
from . import service
from lunardate import LunarDate
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
    new_today = datetime.datetime.now()
    old_today = LunarDate.today()
    tomorrow = datetime.timedelta(days=1)

    peoples = []
    for _i in range(7):
        peoples.append(People.objects.filter(
            (
                Q(birth_lunar__month=old_today.month) &
                Q(birth_lunar__day=old_today.day)
            ) |
            (
                Q(birth_new__month=new_today.month) &
                Q(birth_new__day=new_today.day)
            )
        ))
        new_today += tomorrow
        old_today += tomorrow
    email = service.generateBirthEmail(peoples)
    service.sendEmail(email, '定时任务-生日提醒')
