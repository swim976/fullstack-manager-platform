# -*- coding: utf-8 -*-
import requests
import hashlib
import time
import re
import datetime
from django.conf import settings
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.header import Header


def sendGitCommitSMS(name, repo, phone=settings.ALIDAYU_PHONE):
    '''通过阿里大鱼发送repo提交提醒'''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    parameters = {
        'app_key': settings.ALIDAYU_APP_KEY,
        'format': 'json',
        'method': 'alibaba.aliqin.fc.sms.num.send',
        'rec_num': phone,
        'sign_method': "md5",
        'sms_free_sign_name': settings.ALIDAYU_SMS_FREE_SIGN_NAME,
        'sms_param': '{"name":"' + name + '","repo":"' + repo + '"}',
        'sms_template_code': settings.ALIDAYU_SMS_TEMPLATE_CODE,
        'sms_type': 'normal',
        'timestamp': timestamp,
        'v': '2.0'
    }

    # 生成签名
    if hasattr(parameters, "items"):
        keys = list(parameters.keys())
        keys.sort()

        parameters_str = "%s%s%s" % (
            settings.ALIDAYU_APP_SECRET,
            str().join('%s%s' % (key, parameters[key]) for key in keys),
            settings.ALIDAYU_APP_SECRET)
    parameters['sign'] = \
        hashlib.md5(parameters_str.encode('utf8')).hexdigest().upper()

    re = requests.post(settings.ALIDAYU_URL, headers=headers, data=parameters)
    print(re.text)


def sendEmail(
        content, subject,
        sender=settings.MAIL_USER, receivers=[settings.ADMIN_EMAIL]):
    '''发送邮箱接口'''
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = "\"%s\" <%s>" % (
            Header(sender, 'utf-8'),
            Header(sender, 'utf-8'))
    message['To'] = Header('to', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP()
    smtpObj.connect(settings.MAIL_HOST)
    smtpObj.login(settings.MAIL_USER, settings.MAIL_PASS)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')

def generateBirthEmail(peoples):
    '''生成生日提醒邮件内容'''
    string = '亲，以下是最近快过生日的好友，别忘了送上祝福哟\n'
    print(peoples)
    for _i in range(7):
        if len(peoples[_i]) == 0:
            continue
        if _i == 0:
            string += '\n今天过生日的有: \n'
        elif _i == 1:
            string += '\n明天过生日的有: \n'
        elif _i == 2:
            string += '\n后天过生日的有: \n'
        else:
            string += '\n' + str(_i) + '天后过生日的有: \n'
        for people in peoples[_i]:
            string += str(people) + '\n'
    return string

def getLunar():
    '''获取农历日期'''
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
    return int(months.index(month)), int(days.index(day))

def getNextDate(month, day, next):
    '''获取接下来几天的日期，特殊需要，没有用datetime，不过next小于7，下一个闰年在2020年,so'''
    day = day + next
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if(day > 31):
            day -= 31
            month += 1
    elif month == 2:
        if(day > 28):
            day -= 28
            month += 1
    else:
        if(day > 30):
            day -= 30
            month += 1
    if month > 12:
        month = 1

    return month, day


if __name__ == '__main__':
    sendEmail()
