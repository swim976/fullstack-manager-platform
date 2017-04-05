import requests

from django.conf import settings


class Smzdm:
    """
    什么值得买自动签到脚本
    """
    def __init__(self):
        self.session = requests.Session()

        self.open_site()
        self.login()
        self.open_site_again()
        self.check_in()

        print('签到成功')

    def open_site(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.88 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
            'Host': 'www.smzdm.com'
        }

        self.session.get(url='http://www.smzdm.com/', headers=headers)

    def login(self):
        login_headers = {
            'Pragma': 'no-cache',
            'Origin': 'https://zhiyou.smzdm.com',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,ja;q=0.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.88 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Cache-Control': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'connection': 'keep-alive',
            'Referer': 'https://zhiyou.smzdm.com/user/login/window/'
        }
        login_data = {
            'username': settings.SMZDM_USER,
            'password': settings.SMZDM_PASS,
            'rememberme': '0',
            'captcha': '',
            'redirect_to': '',
            'geetest_challenge': '',
            'geetest_validate': '',
            'geetest_seconde': ''
        }
        self.session.post(url='https://zhiyou.smzdm.com/user/login/ajax_check', data=login_data, headers=login_headers)

    def open_site_again(self):
        headers = {
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,ja;q=0.2',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.88 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Cache-Control': 'no-cache',
            'connection': 'keep-alive',
        }
        r = self.session.get(url='http://www.smzdm.com/', headers=headers)

        assert self.session.cookies['user'] == 'user%3A8361849767%7C8361849767'

    def check_in(self):
        headers = {
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,ja;q=0.2',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.88 Safari/537.36',
            'Accept': '*/*',
            'Referer': 'http://www.smzdm.com/',
            'Cache-Control': 'no-cache',
            'connection': 'keep-alive'
        }
        r = self.session.get(url='http://zhiyou.smzdm.com/user/checkin/jsonp_checkin?callback=jQuery11240362928107545587_1488940974679&_=1488940974681', headers=headers)
        print(r.text)   # jQuery11240362928107545587_1488940974679({"error_code":0,"error_msg":"","data":{"add_point":0,"checkin_num":"130","point":4359,"exp":5478,"gold":4,"prestige":0,"rank":14,"slogan":"<div class=\"signIn_data\">\u4eca\u65e5\u5df2\u9886<span class=\"red\">30<\/span>\u79ef\u5206<\/div>"}})

if __name__ == '__main__':
    Smzdm()
