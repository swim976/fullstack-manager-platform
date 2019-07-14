import subprocess
import time

from cron.android import _begin
from cron.cron import Cron


class Smzdm(Cron):
    symbol = "ANDROID_SMZDM"
    description = "什么值得买签到"
    CRONTAB_COMMENT = description

    def __init__(self):
        super().__init__()
        self.run()

    def run(self):
        cmds = {
            "打开什么值得买": "adb shell am start -n com.smzdm.client.android/com.smzdm.client.android.activity.HomeActivity",
            "点击右下角我的(可能有弹窗)": "adb shell input tap 700 1200",
            "点击右下角我的": "adb shell input tap 700 1200",
            "点击签到领奖": "adb shell input tap 551 463",
            # TODO: 判断是否出现"签到成功"
        }
        _begin()
        for step, cmd in cmds.items():
            print(step + ": " + cmd)
            subprocess.check_output(cmd, shell=True)
            time.sleep(20)


if __name__ == "__main__":
    Smzdm()
