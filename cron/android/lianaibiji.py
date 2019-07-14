import time

from cron.android import _begin, _exec, _get_text_in_screen, _ocr_screen
from cron.cron import Cron


class Lianaibiji(Cron):
    symbol = "ANDROID_LIANAIBIJI"
    description = "恋爱笔记签到"
    CRONTAB_COMMENT = description

    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        _begin()

        _exec(
            "adb shell am start -n com.lianaibiji.dev/.ui.start.load.LoadActivity",
            120,
            "打开恋爱笔记",
        )

        print("判断是否有每日一句")
        result = _get_text_in_screen("每日一句")
        if result is not None:
            _exec("adb shell input tap 360 1158", 5)

        _exec("adb shell input tap 380 1044", 10, "点击悄悄话")
        _exec('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "我爱你"', 5, "发送文字")
        _exec("adb shell input tap 592 1209", 30, "点击发送")
        _exec("adb shell input keyevent KEYCODE_BACK", 10, "关闭确认窗口")
        _exec("adb shell input keyevent KEYCODE_BACK", 10, "返回应用主页")
        _exec("adb shell input tap 16 350", 60, "点击打卡挑战")

        screen = _ocr_screen()
        if screen.get_text_location("新建一篇恋爱笔记") is not None:
            for word in screen.result["words_result"]:
                if "题:" in word["words"]:
                    topic = word["words"].split(":")[1].replace(")", "")
                    _exec("adb shell input keyevent KEYCODE_BACK", 5, "返回去新建恋爱笔记")
                    _exec("adb shell input tap 140 1080", 5, "点击恋爱记录")
                    _exec("adb shell input tap 670 90", 5, "右上角新建记录")
                    _exec(
                        f'adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{topic}:未来有你"',
                        1,
                        "输入文字",
                    )
                    _exec("adb shell input tap 670 90", 60, "右上角发送")
        else:
            assert 1 is None

        print("确认已经完成")
        assert _get_text_in_screen("你的恋爱任务已完成") is not None


if __name__ == "__main__":
    Lianaibiji()
