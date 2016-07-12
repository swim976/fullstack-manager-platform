# -*- coding: utf-8 -*-
import re
import time
import codecs
import random
import hashlib
import smtplib
import requests
import datetime
from bs4 import BeautifulSoup
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from django.conf import settings


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


def captureKuaidaili():
    '''抓取快代理页面'''
    urls = [
        # 'http://www.kuaidaili.com/free/inha/',      # 国内高匿代理
        # 'http://www.kuaidaili.com/free/intr/',      # 国内普通代理
        # 'http://www.kuaidaili.com/free/outha/',     # 国外高匿代理
        'http://www.kuaidaili.com/free/outtr/',     # 国外普通代理
    ]
    headers = {
        'Accept': 'text/html,application/xhtml+xml,\
                                application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;\
                                q=0.2,ja;q=0.2',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) \
                                AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/49.0.2623.110 Safari/537.36',
        'Referer': 'http://www.kuaidaili.com/free/outtr/1/',
        'Connection': 'keep-alive'
    }
    fp = codecs.open('url.txt', 'w', 'utf-8')
    for url in urls:
        page = 964
        all_page = 0    # 总的页数
        headers['Referer'] = url
        while True:
            time.sleep(random.randint(0, 10))
            retry = 1
            while True:
                fp.write(url + str(page) + '\n')
                print(url + str(page))
                re = requests.get(
                                settings.SPLASH + url + str(page),
                                headers=headers)

                if 'setTimeout' not in re.text and \
                        'GlobalTimeoutError' not in re.text:
                    print('the response content is ok.')
                    break
                else:
                    print(re.text)
                    if retry == 10:
                        print('retry times too much, fuck this site:' + url)
                    retry += 1
                    time.sleep(random.randint(0, 10))
            print(url + str(page) + ': finished')

            soup = BeautifulSoup(re.content)
            try:
                tr_tags = soup.find('tbody').find_all('tr')
            except AttributeError:
                print('the tag not found.')
                print(re.content)
                break

            for tr_tag in tr_tags:
                td_tags = tr_tag.find_all('td')
                data = {
                    'ip': td_tags[0].string,
                    'port': td_tags[1].string,
                    'anonymity': td_tags[2].string,
                    'http': td_tags[3].string,
                    'action': '',
                    'address': td_tags[4].string,
                    'site': 'http://www.kuaidaili.com/'
                }
                yield data

            # 判断终止条件
            if all_page == 0:
                list_nav_tag = soup.select('div#listnav')[0]
                a_tags = list_nav_tag.find_all('a')
                page_list = [int(a_tag.string) for a_tag in a_tags]
                all_page = max(page_list)
            elif page == all_page:
                break
            else:
                page += 1


if __name__ == '__main__':
    sendEmail()
