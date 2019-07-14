import time
import subprocess

from cron.android.ocr import Ocr


def _exec(cmd, sleep=1, desc=None):
    if desc is not None:
        print(desc)
    result = subprocess.check_output(cmd, shell=True).decode("utf-8")
    time.sleep(1)
    return result


def _tap(x, y):
    cmd = f"adb shell input tap {x} {y}"
    return _exec(cmd)


def _wakeup():
    """唤醒屏幕"""
    print("唤醒屏幕")
    cmd = "adb shell dumpsys power | grep mScreenOn"
    result = _exec(cmd)
    if "mScreenOn=true" not in result:
        cmd = "adb shell input keyevent KEYCODE_POWER"
        result = _exec(cmd)
    return result


def _clear_cache():
    """清理运存"""
    print("清理运存")
    _exec("adb shell input keyevent KEYCODE_HOME", 5)
    _exec("adb shell input keyevent KEYCODE_APP_SWITCH", 5)
    _exec("adb shell input tap 360 1158", 5)


def _begin():
    """执行任务前的预备操作: 点亮屏幕 清理运存"""
    print("任务预备")
    _wakeup()
    _clear_cache()


def _get_text_in_screen(text):
    """通过ocr验证文字肯定存在屏幕中"""
    print("截图验证")
    return _ocr_screen().get_text_location(text)


def _ocr_screen():
    """返回ocr识别的结果"""
    print("ocr识别")
    name = time.strftime("%Y%m%d%H%M%S")
    _exec(f"adb shell /system/bin/screencap -p /sdcard/{name}.png")
    _exec(f"adb pull /sdcard/{name}.png /tmp")
    return Ocr(f"/tmp/{name}.png")


if __name__ == "__main__":
    # _wakeup()
    _begin()
