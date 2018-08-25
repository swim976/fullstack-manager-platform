# 数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'admin',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '192.168.0.4',
        'PORT': 3306
    }
}

# 定时任务
CRONJOBS = [
    ('* * 31 * *', 'cron.reminder.birthday.Birth'),
    ('* * 31 * *', 'cron.sign.smzdm.Smzdm'),
    ('* * 31 * *', 'cron.backup.database.Database'),
]

BACKUP_DIR = '/data/backup/'
