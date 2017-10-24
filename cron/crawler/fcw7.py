import re, requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.db import connection

from cron.crawler.Crawler import Crawler
from cron.models import CrawlerLog, CrawlerTarget
from service.exceptions import ConflictException


class Fcw7(Crawler):
    """
    视频网站，为防止被ban，不用并发，另外，首次抓取不用you-get
    """
    crawler_target = CrawlerTarget.objects.get(pk=1)
    url_prefix = 'http://www.fcw7.com/latest-updates/'
    s = requests.Session()
    splash_har_url = settings.SPLASH_HAR_URL + 'timeout=600&wait=10&proxy=socks5://' + settings.SOCKS5_PROXY + '&url='
    splash_html_url = settings.SPLASH_HTML_URL + 'timeout=600&wait=10&proxy=socks5://' + settings.SOCKS5_PROXY + '&url='

    def __init__(self):
        super().__init__()

        for index in range(1, 160):
            page_url = self.url_prefix + str(index) + '/'
            try:
                self.insert_crawler_log(page_url, 'html', '最新视频', str(index))
            except ConflictException as e:
                print('repeated url for: ' + page_url)
                continue

            response = self.s.get(self.splash_html_url + page_url)
            self.update_crawler_log(CrawlerLog.objects.latest('id'), response.status_code)

            soup = BeautifulSoup(response.text, 'lxml')
            for item in soup.select('div.item'):
                try:
                    match = re.search('(.*?)分:(.*?)秒', item.select('div.duration')[0].string)
                    minute, second = int(match.group(1)), int(match.group(2))
                    if minute < 5 or minute > 60:    # 小于5分钟的和大于90分钟的都不用
                        continue
                    else:
                        title = item.select('.title')[0].string.strip()
                        url = item.select('a')[0]['href']
                        duration = minute * 60 + second
                        self.get_one(url, title, duration)
                except Exception as e:
                    print(item)
                    print(e)
                    exit(0)

                break
            break

    def get_one(self, url, title, duration):
        """
        下载单个视频
        :param url: 视频页面链接
        :param title: 视频标题
        :param duration: 视频时长，以s为单位
        """
        # 请求页面获取视频链接
        try:
            self.insert_crawler_log(url=url, type='har', tag=url.split('videos/')[1].split('/')[0])
        except ConflictException as e:
            print('repeated url for: ' + url)
            return

        response = self.s.get(self.splash_har_url + url)
        self.update_crawler_log(
            crawler_log=CrawlerLog.objects.latest('id'),
            http_code=response.status_code,
            title=response.json()['log']['pages'][0]['title']
        )

        video_url = video_type = ''
        for entry in response.json()['log']['entries']:
            if 'cv=' in entry['request']['url']:
                video_url = entry['request']['url']
                video_type = entry['response']['content']['mimeType'].split('/')[1]
                break

        # 请求视频链接下载视频
        if video_url:
            try:
                self.insert_crawler_log(url=video_url, type=video_type, tag=url.split('videos/')[1].split('/')[0])
            except ConflictException as e:
                print('repeated url for: ' + url)
                return

            response = self.s.get(video_url, stream=True)
            with open(title + '.' + video_type, 'wb') as fp:
                for chunk in response.iter_content(1024):
                    fp.write(chunk)

            self.update_crawler_log(
                crawler_log=CrawlerLog.objects.latest('id'),
                http_code=response.status_code,
                title=title
            )

            self.insert_crawler_video_log(
                crawler_log=CrawlerLog.objects.latest('id'),
                title=title,
                type=video_type,
                duration=duration
            )
            print('ok')
        else:
            print('video url not found')
            exit(0)

if __name__ == '__main__':
    Fcw7()
