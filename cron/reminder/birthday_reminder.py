import datetime

from django.db.models import Q
from django.conf import settings
from lunardate import LunarDate
from people.models import People
from service.email_service import send_email


def check_birth():
    """
    查询明天生日的人，百度查询，今天是农历几月几日
    """
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
    email = generate_birth_email(peoples)
    send_email(email, '好友生日提醒', settings.CRON_MAIL)


def generate_birth_email(peoples):
    """
    生成生日提醒邮件
    :param peoples:
    :return:
    """
    string = '亲，以下是最近快过生日的好友，别忘了送上祝福哟\n'
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

if __name__ == '__main__':
    check_birth()