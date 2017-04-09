from django.db import models


class Log(models.Model):
    """
    定时任务日志

    CREATE TABLE `cron_log` (
      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
      `symbol` varchar(50) NOT NULL DEFAULT '',
      `successful` tinyint(1) NOT NULL,
      `stdout` text NOT NULL,
      `stderr` text NOT NULL,
      `begin_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
      `end_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    symbol = models.CharField('定时任务标识', max_length=50)
    stdout = models.TextField('标准输出')
    stderr = models.TextField('错误输出')
    successful = models.BooleanField('定时任务是否成功')
    begin_at = models.DateTimeField('定时任务开始时间')
    end_at = models.DateTimeField('定时任务结束时间')

    def __str__(self):
        return self.name + str(self.begin_at)
