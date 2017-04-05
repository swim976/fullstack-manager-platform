# -*- coding: utf-8 -*-
import datetime
import re
import requests
from people.models import People
from django.db.models import Q
from django.db.utils import IntegrityError
from . import service
from .models import Proxy
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




def captureProxy():
    '''抓取快代理的代理'''
    def bulkWork(data_bulk):
        while True:
            if len(data_bulk) == 0:
                return True
            try:
                Proxy.objects.bulk_create(data_bulk)
                break
            except IntegrityError as e:
                match = re.search('Duplicate entry \'(.*?)\'', str(e))
                duplicate_ip = match.group(1)
                data_bulk = [
                    data for data in data_bulk if duplicate_ip != str(data)]

    data_bulk = []  # 100条插入一次
    Proxy.objects.bulk_create(data_bulk)
    for data in service.captureKuaidaili():
        data_bulk.append(Proxy(
            site=data['site'],
            ip=data['ip'],
            port=data['port'],
            anonymity=data['anonymity'],
            http=data['http'],
            action=data['action'],
            address=data['address']
        ))

        if len(data_bulk) == 50:
            bulkWork(data_bulk)
            data_bulk = []
    bulkWork(data_bulk)
