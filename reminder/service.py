# -*- coding: utf-8 -*-
import requests
import hashlib
import time
from django.conf import settings


def sendGitCommitSMS(name, repo, phone=settings.ALIDAYU_PHONE):
    '''通过阿里大鱼发送repo提交提醒'''
    print('enter')
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

    re = requests.post(url, headers=headers, data=parameters)
    result = re.text
    print('out')
