import smtplib

from email.header import Header
from email.mime.text import MIMEText
from django.conf import settings


def send_email(
        content, subject,
        sender, receivers=None):
    """
    发送邮件
    :param content: 邮件内容
    :param subject: 邮件主题
    :param sender: 发送者信息
    :param receivers: 接收者，默认为管理员邮箱
    :return: 
    """
    if receivers is None:
        receivers = [settings.ADMIN_EMAIL]

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = "\"%s\" <%s>" % (
            Header(sender['USER'], 'utf-8'),
            Header(sender['USER'], 'utf-8'))
    message['To'] = Header('to', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(sender['HOST'])
    smtp.login(sender['USER'], sender['PASS'])
    smtp.sendmail(sender['USER'], [receivers], message.as_string())
    print('邮件发送成功')

if __name__ == '__main__':
    import sys
    sys.path.append('/usr/src/app/admin')
    from settings_secret import CRON_MAIL, ADMIN_EMAIL
    send_email('content', 'subject', CRON_MAIL, ADMIN_EMAIL)