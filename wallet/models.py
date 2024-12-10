# 导入动作模块
import time

from ascript.android import action
# 导入节点检索模块
from ascript.android import node

from airscript.intent import Intent
from ascript.android.system import R
from android.net import Uri
from android.provider import Settings
from ascript.android.node import Selector
import requests
import re

# -------------------------------停止app(包名)-------------------------------
def stop_app_click_ok():
    print(f'stop_app_click_ok--')
    while True:
        res = Selector().text("强行停止").clickable(True).find()
        if res is not None:
            print(f'点击强行停止')
            res.click()
            time.sleep(0.5)
            return

        res = Selector().text("确定").find()
        if res is not None:
            print(f'点击确定')
            res.click()
            time.sleep(0.5)
            return

        time.sleep(0.5)

def stop_app_click():
    print(f'stop_app_click--')
    jc = 0
    while True:
        res = Selector().text("强行停止").find()
        if res is not None:
            print(f'点击强行停止')
            jc += 1
            res.click()
            time.sleep(0.5)

        res = Selector().text("结束运行").find()
        if res is not None:
            print(f'点击结束运行')
            jc += 1
            res.click()
            time.sleep(0.5)

        res = Selector().text("取消").find()
        if res is not None:
            print(f'准备二次确认')
            stop_app_click_ok()
            return

        if jc >= 3:
            print(f'应用是停止状态')
            return
        time.sleep(0.5)


# 停止app(包名)
def stop_app(app_package: str):
    print(f"stop_app--")
    while True:
        # 根据需求改变包名,即可跳转,跳转后,可点击停止程序等等.
        intent = Intent(Settings.ACTION_APPLICATION_DETAILS_SETTINGS).setData(
            Uri.fromParts("package", app_package, None))
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        R.context.startActivity(intent);
        time.sleep(0.5)
        print(f'等待界面应用详情进入')
        res = Selector().text("打开").find()
        if res is not None:
            print(f'进入了应用详情')
            stop_app_click()
            time.sleep(0.5)
            action.Key.home()
            time.sleep(0.5)
            return
# # -------------------------------获取验证码(url)---------------------------------
def VerifyCode(url):
    headers = {

        "^upgrade-insecure-requests": "1^",
        "^Referer": "https://ludamao.net/^",
        "^User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36^",
        "^referer": "https://ludamao.net/^",
        "^Origin": "https://ludamao.net^"
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    html = response.text
    # print(html)
    verify_code_elements = re.findall(r'<input[^>]*id="code"[^>]*value="([^"]*)"', html)
    if len(verify_code_elements) > 0:
        verify_code = verify_code_elements[0]
        print(f"获取验证码成功:{verify_code}")
        return verify_code
    else:
        print("获取验证码失败")
        return None


