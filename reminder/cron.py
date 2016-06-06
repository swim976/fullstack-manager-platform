# -*- coding: utf-8 -*-
import datetime
import re
import requests
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

    if count != 0:
        print('begin')
        service.sendGitCommitSMS('haofly', 'admin or haoflynet')

if __name__ == '__main__':
    checkGithub()
