from django.db import models
from django.db.models import DO_NOTHING

CONTENT_TYPE = (
    ('html', 'html'),
    ('video', 'video'),
    ('javascript', 'javascript'),
    ('css', 'css'),
)

VIDEO_TYPE = (
    ('mp4', 'mp4'),
)

SITE_TYPE = (
    ('video', 'video'),
)



class CrawlerTarget(models.Model):
    """
    爬虫目标

    CREATE TABLE `cron_crawler_target` (
      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
      `site` varchar(255) NOT NULL DEFAULT '' COMMENT '目标网站域名',
      `type` varchar(10) NOT NULL DEFAULT '' COMMENT '网站类型(video)',
      `description` varchar(255) NOT NULL DEFAULT '' COMMENT '描述',
      `depend_on_js` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否依赖于js的生成',
      `beta` text NOT NULL COMMENT '要点(比如抓取方式)',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    site = models.CharField('目标网站域名', max_length=255)
    type = models.CharField('网站类型', choices=SITE_TYPE, max_length=10)
    description = models.CharField('描述', max_length=255, default='')
    depend_on_js = models.BooleanField('是否依赖于js的生成')
    beta = models.TextField('要点(比如抓取方式)', default='')

    class Meta:
        db_table = 'cron_crawler_target'


class CrawlerLog(models.Model):
    """
    爬虫日志
    完整的html内容不存储在mysql，直接文件存储

    CREATE TABLE `cron_crawler_log` (
      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
      `target_id` int(11) NOT NULL,
      `url` varchar(500) NOT NULL DEFAULT '' COMMENT '访问过的url',
      `title` varchar(255) NOT NULL DEFAULT '' COMMENT '网站标题',
      `tag` varchar(255) NOT NULL COMMENT '标识',
      `type` varchar(50) NOT NULL DEFAULT '' COMMENT '返回内容类型',
      `http_code` int(3) NOT NULL COMMENT 'HTTP状态码',
      `begin_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '开始时间',
      `end_at` timestamp NULL DEFAULT NULL COMMENT '结束时间',
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    target = models.ForeignKey(CrawlerTarget, on_delete=DO_NOTHING)
    url = models.CharField('访问过的url', max_length=500)
    title = models.CharField('网站标题', max_length=255)
    tag = models.CharField('该url在该网站的标识(例如uuid等)', max_length=255)
    type = models.CharField('返回内容类型', choices=CONTENT_TYPE, max_length=50)
    http_code = models.CharField('http状态码', null=True, max_length=3)
    begin_at = models.DateTimeField('爬虫抓取时间')
    end_at = models.DateTimeField('爬虫结束时间')

    class Meta:
        db_table = 'cron_crawler_log'
