from aip import AipOcr

from admin.settings_test import (
    BAIDU_OCR_APP_ID,
    BAIDU_OCR_API_KEY,
    BAIDU_OCR_SECRET_KEY,
)


class Ocr:
    result = None

    def __init__(self, img_path, app_id=None, api_key=None, secret_key=None):
        with open(img_path, "rb") as fp:
            self.img = fp.read()
        self.client = AipOcr(
            app_id if app_id is not None else BAIDU_OCR_APP_ID,
            api_key if api_key is not None else BAIDU_OCR_API_KEY,
            secret_key if secret_key is not None else BAIDU_OCR_SECRET_KEY,
        )
        self.recognize()

    def recognize(self):
        """进行识别返回识别结果"""
        self.result = self.client.general(self.img)

    def get_result(self):
        return self.result["words_result"]

    def get_text_location(self, text):
        """获取文本在图片中出现的location，包括width,top,height,left，没有则返回None。只返回第一次出现的位置"""
        print(self.result["words_result"])
        for word in self.result["words_result"]:
            if text in word["words"]:
                return word["location"]
        return None


if __name__ == "__main__":
    re = Ocr("/Users/haofly/Downloads/垃圾流量识别2_0.png").get_text_location("评定")
    print(re)
