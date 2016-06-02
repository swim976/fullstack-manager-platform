# -*- coding: utf-8 -*-
import requests
import hashlib


def sendGitCommitSMS(phone, name, repo):
    '''通过阿里大鱼发送repo提交提醒'''
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    parameters = {
        'app_key': '',
        'format': 'json',
        'method': 'alibaba.aliqin.fc.sms.num.send',
        'rec_num': phone,
        'sign_method': "md5",
        'sms_free_sign_name': '',
        'sms_param': '{"name":"' + name + '","repo":"' + repo + '"}',
        'sms_template_code': '',
        'sms_type': 'normal',
        'timestamp': timestamp,
        'v': '2.0'
    }

    # 生成签名
    if hasattr(parameters, "items"):
        keys = list(parameters.keys())
        keys.sort()

        parameters = "%s%s%s" % (
            '',
            str().join('%s%s' % (key, parameters[key]) for key in keys),
            '')
    parameters['sign'] = \
        hashlib.md5(parameters.encode('utf8')).hexdigest().upper()

    re = requests.post(url, headers=headers, data=parameters)
    result = re.text
