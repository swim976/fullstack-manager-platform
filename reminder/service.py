# -*- coding: utf-8 -*-
import requests
import hashlib
import time
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
        'sms_free_sign_name': settings.ALIDAYU_sms_free_sign_name,
        'sms_param': '{"name":"' + name + '","repo":"' + repo + '"}',
        'sms_template_code': settings.ALIDAYU_sms_template_code,
        'sms_type': 'normal',
        'timestamp': timestamp,
        'v': '2.0'
    }

    # 生成签名
    if hasattr(parameters, "items"):
        keys = list(parameters.keys())
        keys.sort()

        parameters = "%s%s%s" % (
            settings.ALIDAYU_APP_SECRET,
            str().join('%s%s' % (key, parameters[key]) for key in keys),
            settings.ALIDAYU_APP_SECRET)

    parameters['sign'] = \
        hashlib.md5(parameters.encode('utf8')).hexdigest().upper()

    re = requests.post(url, headers=headers, data=parameters)
    result = re.text
