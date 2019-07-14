import time
import subprocess


def _exec(cmd):
    return subprocess.check_output(cmd, shell=True).decode("utf-8")


def _tap(x, y):
    cmd = f"adb shell input tap {x} {y}"
    return _exec(cmd)


def _wakeup():
    """唤醒屏幕"""
    print('唤醒屏幕')
    cmd = "adb shell dumpsys power | grep mScreenOn"
    result = _exec(cmd)
    if "mScreenOn=true" not in result:
        cmd = "adb shell input keyevent KEYCODE_POWER"
        result = _exec(cmd)
    return result


def _clear_cache():
    """清理运存"""
    print('清理运存')
    _exec("adb shell input keyevent KEYCODE_HOME")
    time.sleep(5)
    _exec("adb shell input keyevent KEYCODE_APP_SWITCH")
    time.sleep(5)
    _exec("adb shell input tap 360 1158")
    time.sleep(5)


def _begin():
    """执行任务前的预备操作: 点亮屏幕 清理运存"""
    print('任务预备')
    _wakeup()
    time.sleep(1)
    _clear_cache()


if __name__ == "__main__":
    # _wakeup()
    _begin()
