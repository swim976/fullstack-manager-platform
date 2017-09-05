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
        command = 'mysqldump -u{user} -p{password} --databases -h{host} {database} | gzip > {target}'.format(
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            database=settings.DATABASES['default']['NAME'],
            target=settings.BACKUP_DIR + 'mysql/' + str(datetime.date.today()) + '.sql.gz'
        )
        re = subprocess.check_output(command, shell=True)
        print(re)