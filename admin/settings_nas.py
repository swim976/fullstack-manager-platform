# 定时任务
CRONJOBS = [
    ('30 11 * * *', 'cron.reminder.birthday.Birth'),
    ('0 1 * * *', 'cron.sign.smzdm.Smzdm'),
    ('0 5 * * *', 'cron.backup.database.Database'),
    ('0 10 * * *', 'cron.crawler.fcw7.Fcw7'),
]

# database备份目录
BACKUP_DIR = '/data/backup/'

# Sockes5代理
SOCKS5_PROXY = '192.168.0.8:1086'

# SPLASH服务
SPLASH_HAR_URL = 'http://192.168.0.9:8050/render.har?'
SPLASH_HTML_URL = 'http://192.168.0.9:8050/render.html?'
SPLASH_HTTPS_HAR_URL = 'http://192.168.0.9:8051/render.har?'
SPLASH_HTTPS_HTML_URL = 'http://192.168.0.9:8051/render.html？'
