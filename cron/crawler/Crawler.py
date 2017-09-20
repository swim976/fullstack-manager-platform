import datetime

from cron.models import CrawlerLog, CrawlerVideoLog, CrawlerTarget
from service.exceptions import ConflictException


class Crawler:
    """
    爬虫基类，主要用于记录日志
    """
    crawler_target = CrawlerTarget()

    def __init__(self):
        pass

    def insert_crawler_log(self, url, type=None, title=None, tag=None):
        """
        记录爬虫日志
        :return:
        """
        if CrawlerLog.objects.filter(url=url).exclude(end_at=None).first() is None:
            crawler_log = CrawlerLog(
                target_id=self.crawler_target.id,
                url=url,
                begin_at=datetime.datetime.today()
            )
            crawler_log.title = None if title is None else title
            crawler_log.type = None if type is None else type
            crawler_log.tag = None if tag is None else tag

            crawler_log.save()
        else:
            raise ConflictException('repeated url for ' + url)

    def update_crawler_log(self, crawler_log, http_code=None, type=None, title=None, tag=None):
        """
        请求结束时更新爬虫日志
        :param id:
        :param http_code:
        :return:
        """
        crawler_log.http_code = crawler_log.http_code if http_code is None else http_code
        crawler_log.type = crawler_log.type if type is None else type
        crawler_log.title = crawler_log.title if title is None else title
        crawler_log.tag = crawler_log.tag if tag is None else tag
        crawler_log.end_at = datetime.datetime.today()
        crawler_log.save()

    def insert_crawler_video_log(self, crawler_log, title=None, type=None, duration=0):
        """
        记录视频爬虫额外信息
        :return:
        """
        CrawlerVideoLog(
            crawler_id=crawler_log.id,
            title=title,
            type=type,
            duration=duration
        ).save()