# -*- coding: utf-8 -*-
import datetime
import re
import requests
#from . import service
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
    url = 'https://www.baidu.com/s'
    params = {
        'ie': 'utf-8',
        'f': '8',
        'rsv_bp': '1',
        'tn': 'baidu',
        'wd': '今天是农历几月几日',
        'oq': '今天是农历几月几日',
        'rsv_pq': 'bf14469c00210a2d',
        'rsv_t': 'dd6cJS7L8heOZxh2qjKYMqdjYTBoWZq+cM9MUxWIN2Hu3ewz9C8v3fYL2JI',
        'rqlang': 'cn',
        'rsv_enter': '1',
        'rsv_sug3': '1',
        'rsv_sug1': '1',
        'rsv_sug7': '100',
        'bs': '今天是农历几月几日'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
    }
    r = requests.get(url, params=params, headers=headers)
    match = re.search('<div class="op-calendar-title c-gray">万年历</div>([\s\S]*?)<span>([\s\S]*?)<span>(?P<date>[\s\S]*?)</span>', r.text)
    date = match.group('date') \
                .replace(' ', '').replace('\n', '').split('农历')[1]
    month, day = date.split('月')
    months = [
            '农历月', '一', '二', '三', '四', '五', '六',
            '七', '八', '九', '十', '十一', '十二']
    days = [
            '农历天', '初一', '初二', '初三', '初四', '初五', '初六', '初七',
            '初八', '初九', '初十', '十一', '十二', '十三', '十四', '十五', '十六',
            '十七', '十八', '十九', '二十', '廿一', '廿二', '廿三', '廿四', '廿五',
            '廿六', '廿七', '廿八', '廿九', '三十']
    month = months.index(month)
    day = days.index(day)
    print(month, day)




if __name__ == '__main__':
    checkBirth()
