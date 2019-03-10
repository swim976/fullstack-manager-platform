import datetime
import subprocess

from cron.cron import Cron
from django.conf import settings


class Database(Cron):
    symbol = 'BACKUP_DATABASE'
    description = '数据库备份'
    CRONTAB_COMMENT = description

    def __init__(self):
        super().__init__()

        # 备份nas数据库
        command = 'mysqldump -u{user} -p{password} --databases -h{host} {backupdb} | gzip > {target}'.format(
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            backupdb=settings.BACKUP_BACKUP_DB_NAS,
            target=settings.BACKUP_DIR + 'mysql/nas' + str(datetime.date.today()) + '.sql.gz'
        )
        re = subprocess.check_output(command, shell=True)
        print(re)

        # 备份ali数据库
        command = 'mysqldump -u{user} -p{password} --databases -h{host} {backupdb} | gzip > {target}'.format(
            user=settings.DATABASES['ali']['ALI_USER'],
            password=settings.DATABASES['ali']['PASSWORD'],
            host=settings.DATABASES['ali']['HOST'],
            backupdb=settings.BACKUP_DB_ALI,
            target=settings.BACKUP_DIR + 'mysql/ali' + str(datetime.date.today()) + '.sql.gz'
        )
        re = subprocess.check_output(command, shell=True)
        print(re)