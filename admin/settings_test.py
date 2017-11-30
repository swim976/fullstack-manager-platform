# 定时任务
CRONJOBS = [
    ('* * 31 * *', 'cron.reminder.birthday.Birth'),
    ('* * 31 * *', 'cron.sign.smzdm.Smzdm'),
    ('* * 31 * *', 'cron.backup.database.Database'),
]

BACKUP_DIR = '/data/backup/'