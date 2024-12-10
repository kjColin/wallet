from ascript.android import action
# from ascript.android import action.Hid
from ascript.android.node import Selector
from ..emailcode import email_code
import time
from ascript.android import system
from .models import VerifyCode, stop_app
from ascript.android.system import R
from ascript.android.system import Device


# 回退到tg主界面
def back_to_tg_main():
    print(f'back_to_tg_main--')
    jc = 0
    while True:
        if jc > 60:
            print(f'界面不存在')
            return
        res = Selector().desc("New Message").type("FrameLayout").clickable(True).find()
        if res is not None:
            print(f'回到了tg主界面')
            # exit_account()
            return

        action.Key.back()
        time.sleep(1.5)
        jc += 1


def ton_space():
    print(f'ton_space--')
    jc = 0  # 初始化搜索计数器
    while True:
        # 检查超时
        if jc > 60:
            print("ton_space操作超时")
            # main()
            return
        res = Selector().text("Wallet Balance").type("TextView").find()
        if res is not None:
            print('找到余额')

        res = Selector().text("Wallet Balance").type("TextView").clickable(False).parent(2).brother(1).child(1).find()
        if res is not None:
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(1)
            print("setting")

        res = Selector().text("钱包语言").find() 
        if res is not None:
            res.click()
            time.sleep(2)
            print("language")
        
            res = Selector().text("English").type("TextView").parent(1).find()
            if res is not None:
                res.click()
                time.sleep(2)
                print("English")
                action.Key.back()


        res = Selector().text("PasscodeSet Up").type("View").find()
        if res is not None:
            action.click(950, 314)
            time.sleep(2)
            print("ton space start")
            action.Key.back()
            time.sleep(2)
        res = Selector().text("Wallet Balance").type("TextView").find()
        if res is not None:
            print('找到余额')
            backup()
            return
        time.sleep(0.5)
        jc += 1
# 备份

def backup():
    print(f'backup--')
    jc = 0  # 初始化搜索计数器
    while True:
        # 检查超时
        if jc > 60:
            print("backup email操作超时")
            # main()
            return

        res = Selector().text("TON Space").parent(2).find() or Selector().text("TON空间").find()
        if res is not None:
            res.click()
            time.sleep(1)
            print("TON space")

        # 判断是否已经备份过
        res = Selector().text("Deposit").find()
        if res is not None:
            print('已经备份过')
            back_to_tg_main()
            return
        # 判断是否已经创建过钱包
        res = Selector().text("Create or import another wallet").find()
        if res is not None:
            print('已经备份过钱包')
            back_to_tg_main()
            return
            # 点击创建钱包

        res = Selector().text("Start Exploring TON").type("Button").find()
        if res is not None:
            res.click()
            time.sleep(1)
            print("start exploring")

        res = Selector().text("Back Up via Email").type("Button").find()
        if res is not None:
            res.click()
            time.sleep(1)
            print("backup")

        res = Selector().text("Your email address").parent(1).find()
        if res is not None:
            action.click(540, 1210)
            action.input('baibai5845203344@qq.com')
            time.sleep(1)
            print("email input")

            action.click(540, 1800)
            time.sleep(20)

            # 验证码
            verification_code = email_code()
            print(verification_code)
            action.input(verification_code)
            time.sleep(1)
            print("code input")
            back_to_tg_main()
            return
        time.sleep(0.5)
        jc += 1


def wallet_new():
    print(f'wallet_new--')
    jc = 0  # 初始化搜索计数器
    while True:
        # 检查超时
        if jc > 60:
            print("agree terms of use操作超时")
            # main()
            return
        # Click "agree to the Terms of Use" button
        res = Selector().text("I agree to the Terms of Use").type("CheckBox").find()
        if res is not None:
            res.click()
            print("agreed")

            # Click "Continue" button
        time.sleep(1)  # Short wait before finding the next element
        res = Selector().text("Continue").type("TextView").find()
        if res is not None:
            res.click()
            print("continued")

        time.sleep(10)  # Wait for any transitions or loading
        # Try to find and click "Let's go" button
        res = Selector().text("Let's go").find()
        if res is not None:
            res.click()
            print("Let's go clicked")
            time.sleep(5)
            ton_space()
            return
        res = Selector().text("Wallet Balance").type("TextView").find()
        if res is not None:
            print('找到余额')
            ton_space()
            return
        time.sleep(0.5)
        jc += 1


# 判断是否有搜索界面
def search_task():
    print(f'search_task--')
    search_text = 'Wallet'
    jc = 0
    while True:
        if jc > 60:
            print(f'搜索超时')
            # 调用个主函数

            return
        time.sleep(10)
        res = Selector().text("Remind me later").brother(-0.1).find()
        if res is not None:
            res.click()
            time.sleep(0.5)
        
        res = Selector().desc("Search").type("ImageButton").clickable(True).find()
        if res is not None:
            print(f'可以开始搜索')
            res.click()
            time.sleep(0.5)

        res = Selector().text("Search").type("EditText").clickable(True).find()
        if res is not None:
            res.input(search_text)
            time.sleep(0.5)

        print('开始等待搜索结果...')
        timeout = 60  # 设置超时时间为60秒
        elapsed_time = 0  # 经过的时间
        check_interval = 1  # 每次检查间隔为1秒
        while elapsed_time < timeout:
            res = Selector().text("Global search").type("TextView").find() or Selector().text("Chats").find()
            if res:  # 检查res_list是否非空
                print(f'搜索成功')
                break
            else:  # 如果res_list为空，则等待一段时间再检查
                time.sleep(check_interval)  # 等待一段时间再检查
                elapsed_time += check_interval  # 增加经过的时间

        res_list = Selector().text("Wallet").type("ViewGroup").clickable(False).find_all()
        for i in res_list:
            if len(i.text) == 22 or len(i.text) == 26:
                print(f'找到结果：{i.text}')
                res = i
                time.sleep(0.5)
                action.click(res.rect.centerX(), res.rect.centerY())
                time.sleep(10)
                wallet_bot()
                return
        print(f'未找到结果')
        time.sleep(0.5)
        jc += 1


def wallet_bot():
    print(f'wallet_bot--')
    jc = 0  # 初始化搜索计数器
    while True:
        # 检查超时
        if jc > 60:
            print("wallet_bot操作超时")
            # main()
            return
        # Click "agree to the Terms of Use" button
        res = Selector().text("I agree to the Terms of Use").type("CheckBox").find()
        if res is not None:
            res.click()
            print("agreed")

        res = Selector().text("START").type("TextView").clickable(True).find()
        if res is not None:
            res.click()
            time.sleep(1)
            print('start')
        res = Selector().text("Open Wallet").type("Button").find()
        if res is not None:
            res.click()
            time.sleep(1)
            print('open wallet')
            time.sleep(10)

            res = Selector().text("I agree to the Terms of Use").type("CheckBox").find()
            if res is not None:
                # 新用户同意协议
                wallet_new()
                return
            # 判断是否有 ton space beta
            else:
                print('开始检查余额...')
                for _ in range(3):
                    time.sleep(1)
                    res = Selector().text("English").type("View").brother(0.1).find()
                    if res:
                        action.click(res.rect.centerX(), res.rect.centerY())
                        print('选择英语')
                    time.sleep(1)
                    res = Selector().text("OK").find()
                    if res:
                        res.click()
                        print('确认')
                    time.sleep(1)

                timeout = 60  # 设置超时时间（60秒）
                elapsed_time = 0  # 经过的时间
                check_interval = 1  # 每次检查间隔（1秒）

                while elapsed_time < timeout:
                    res = Selector().text("Wallet Balance").type("TextView").find() 
                    if res is not None:
                        print('找到余额')
                        break  # 找到余额后退出循环

                    time.sleep(check_interval)  # 等待一段时间再检查
                    elapsed_time += check_interval  # 增加经过的时间

                # 检查 beta 的存在
                beta = Selector().text("Beta").type("TextView").find() or Selector().text("测试中").find()
                if beta is not None:
                    print('backup')
                    # 连接邮箱备份
                    backup()
                    return
                else:
                    print('ton space 设置')
                    # 设置里调出ton space
                    ton_space()
                    return
        time.sleep(0.5)
        jc += 1


# 输入密码
def input_password():
    pwd = ['Zpaily88', 'qweqwe', 'Zpaily88', 'qweqwe', 'Zpaily88']
    print(f'input_password--')
    jc = 0
    i = 0
    while True:
        if i >= len(pwd):
            print(f'密码输入次数超过限制')
            return  # 超过密码输入次数，退出函数

        if jc > 60:
            print(f'界面不存在')
            return  # 超过尝试次数，退出函数

        res = Selector().text("Your password").type("TextView").clickable(False).brother(0.2).find()
        if res is not None:
            print(f'输入密码')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(0.5)
            action.input(pwd[i])
            time.sleep(1.5)
            res = Selector().desc("Done").type("FrameLayout").clickable(True).find()
            if res is not None:
                print(f'点击完成')
                action.click(res.rect.centerX(), res.rect.centerY())
                print(f'等待3s判断是否登录成功')
                time.sleep(3)
                res = Selector().desc("Search").type("ImageButton").clickable(True).find() or Selector().text("Remind me later").brother(-0.1).find()
                if res:  # 检查res是否为真值
                    search_task()
                    return
                else:
                    print("登录未成功，等待再次检查")
                    # 利用一个循环等待“Search”按钮可用
                    for _ in range(60):  # 最大等待时间为60秒，避免无限循环
                        time.sleep(1)  # 暂停一段时间再检查，可以防止CPU占用过高
                        res = Selector().desc("Search").type("ImageButton").clickable(True).find() or Selector().text("Remind me later").brother(-0.1).find()
                        if res:  # 如果找到了，执行搜索任务
                            search_task()
                            return

            i += 1  # 密码输入失败，尝试下一个密码
        else:
            print("未找到输入框，增加jc以检查界面状态")
            jc += 1  # 增加界面检查次数
        time.sleep(0.5)


# 输入验证码
def input_code(url):
    print(f'input_code--')
    jc = 0
    code = None
    while True:
        if jc > 60:
            print(f'界面不存在')
            return

        res = Selector().type("EditText").depth(4).clickable(True).find()
        if res is not None:
            print(f'输入验证码')
            action.click(res.rect.centerX(), res.rect.centerY())
            for i in range(4):
                print(f'等待30秒获取验证码')
                time.sleep(30)
                code = VerifyCode(url)
                print(f'验证码：{code}')
                if code is not None:
                    time.sleep(0.5)
                    action.input(code)
                    break
                else:
                    time.sleep(10)
                    print(f'验证码获取失败,请更换手机号')

            if code is None:
                print(f'验证码获取失败')
                return

            time.sleep(2)

        res = Selector().text("Your password").type("TextView").clickable(False).find()
        if res is not None:
            print(f'进入了登录界面')
            input_password()
            return
        time.sleep(0.5)
        jc += 1


# 输入账号
def input_account(phone, url):
    print(f'input_account--')
    jc = 0
    while True:
        if jc > 60:
            print(f'界面不存在')
            return
        # res = Selector().desc("Phone number").type("EditText").clickable(True).find()
        res = Selector().desc("Country code").type("EditText").clickable(True).find()
        if res is not None:
            is_phone = Selector().desc("Phone number").type("EditText").clickable(True).find()
            if is_phone is not None:
                if is_phone.text is None:
                    print(f'输入手机号')
                    action.click(res.rect.centerX(), res.rect.centerY())
                    time.sleep(0.5)
                    action.input(phone)
            time.sleep(1.5)
            res = Selector().desc("Done").type("FrameLayout").clickable(True).find()
            if res is not None:
                print(f'点击完成')
                action.click(res.rect.centerX(), res.rect.centerY())
                time.sleep(2)
        res = Selector().text("Yes").type("TextView").clickable(True).find()
        if res is not None:
            print(f'点击确认')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(2)

        res = Selector().text("This phone number is banned.").find()
        if res is not None:
            print(f'账号被封禁')
            # 调用个主函数
            # 记录账号被封禁
            # 退出程序
            return

        res = Selector().text("Continue").type("TextView").clickable(True).find()
        if res is not None:
            print(f'点击继续')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(0.5)

        res = Selector().text("拒绝").type("Button").clickable(True).find()
        if res is not None:
            print(f'点击拒绝')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(0.5)

        # 新弹窗拒绝（第二个弹窗）
        res = Selector().text("拒绝").type("Button").find()
        if res is not None:
            print(f'点击拒绝')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(0.5)
        # 有验证码 input_code
        res = Selector().text("Check your Telegram messages").type("TextView").clickable(False).find()
        if res is not None:
            print(f'进入了输入验证码界面')
            input_code(url)
            time.sleep(0.5)
            return
        # 无验证码，input_password
        res = Selector().text("Your password").type("TextView").clickable(False).brother(0.2).find()
        if res is not None:
            print(f'输入密码界面')
            input_password()
            return
        time.sleep(0.5)
        jc += 1


def get_proxy(phone, url, ip, port, user, password):
    print(f'get_proxy--')
    jc = 0
    while True:
        if jc > 60:
            print(f'界面不存在')
        res = Selector().text("Server").find()
        if res is not None:
            res.input(ip)
            time.sleep(1)
        res = Selector().text("MTProto Proxy").parent(1).brother(0.2).find()
        if res is not None:
            res.click()
            time.sleep(1)
            res.input(port)
            time.sleep(1)
        res = Selector().text("Username").find()
        if res is not None:
            res.input(user)
            time.sleep(1)
        res = Selector().text("Password").find()
        if res is not None:
            res.input(password)
            time.sleep(1)
        res = Selector().desc("Done").find()
        if res is not None:
            res.click()
            time.sleep(1)
        # res = Selector().text("Proxy Settings").find()
        # if res is not None:
        #     action.click(970, 315)
        #     time.sleep(10)
        # res = Selector().text("Save").type("TextView").clickable(True).find()
        # if res is not None:
        #     action.click(res.rect.centerX(), res.rect.centerY())
        #     time.sleep(1)
        #     action.Key.back()
        res = Selector().text("Add Proxy").type("FrameLayout").clickable(False).brother().find()
        if res is not None:
            print(f'点击连接')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(5)

        # 等待直到找到"Connected"
        timeout = 60  # 设置超时时间（60秒）
        elapsed_time = 0  # 经过的时间
        check_interval = 1  # 每次检查间隔（1秒）

        while elapsed_time < timeout:
            res = Selector().text("Connected").find()
            if res is not None:
                print(f'连接成功')
                action.Key.back()
                time.sleep(1)
                input_account(phone, url)
                return

            time.sleep(check_interval)  # 等待一段时间再检查
            elapsed_time += check_interval  # 增加经过的时间

        print(f'等待连接超时，未找到"Connected"')

        time.sleep(0.5)
        jc += 1



# 设置代理
def set_proxy(phone, url, ip, port, user, password):
    print(f'set_proxy--')
    jc = 0
    while True:
        if jc > 60:
            print(f'界面不存在')
            return
        res = Selector().text("Add Proxy").type("FrameLayout").clickable(False).parent(1).child().find_all()
        if res is not None:
            print(f'空间数量：{len(res)}')
            if len(res) > 7:
                res = Selector().text("Add Proxy").type("FrameLayout").clickable(False).parent(1).child(4).find()
                if res is not None:
                    print(res)
                    action.Touch.down(res.center_x, res.center_y)
                    time.sleep(3)
                    action.Touch.up(res.center_x, res.center_y)
                    time.sleep(0.5)

                res = Selector().desc("Go back").type("ImageView").clickable(True).brother(-0.1).child(3).find()
                if res is not None:
                    print(f'点击删除')
                    action.click(res.rect.centerX(), res.rect.centerY())
                    time.sleep(0.5)

                res = Selector().text("Delete").type("TextView").clickable(True).find()
                if res is not None:
                    print(f'点击删除')
                    action.click(res.rect.centerX(), res.rect.centerY())
                    time.sleep(1.5)
            else:
                res = Selector().text("Add Proxy").type("FrameLayout").clickable(False).find()
                if res is not None:
                    print(f'点击添加代理')
                    action.click(res.rect.centerX(), res.rect.centerY())
                    time.sleep(0.5)

                res = Selector().text("Proxy Details").type("TextView").clickable(False).find()
                if res is not None:
                    print(f'进入了设置界面')
                    get_proxy(phone, url, ip, port, user, password)
                    return
            time.sleep(0.5)
            jc += 1


# 设置代理主函数
def set_proxy_main(phone, url, ip, port, user, password):
    print(f'set_proxy_main--')
    jc = 0
    while True:
        if jc > 60:
            print(f'界面不存在')
            return
        res = Selector().desc("Done").type("FrameLayout").clickable(True).brother(-0.1).find()
        if res is not None:
            print(f'点击设置代理')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(0.5)

        res = Selector().text("Proxy Settings").type("TextView").clickable(False).find()
        if res is not None:
            print(f'进入了设置代理界面')
            set_proxy(phone, url, ip, port, user, password)
            return

        res = Selector().text("Continue").type("TextView").clickable(True).find()
        if res is not None:
            print(f'点击继续')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(0.5)

        res = Selector().text("拒绝").type("Button").clickable(True).find()
        if res is not None:
            print(f'点击拒绝')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(0.5)
        time.sleep(0.5)
        jc += 1


def login_account(phone, url, ip, port, user, password):
    print(f'new_login_account--')
    system.open('org.telegram.messenger.web')
    time.sleep(1)
    jc = 0
    while True:
        if jc > 60:
            print(f'界面不存在')
            return
        res = Selector().text("Start Messaging").type("TextView").clickable(True).find()
        if res is not None:
            print(f'点击开始聊天')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(0.5)

        res = Selector().text("Continue").type("TextView").clickable(True).find()
        if res is not None:
            print(f'点击继续')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(0.5)

        res = Selector().text("拒绝").type("Button").clickable(True).find()
        if res is not None:
            print(f'点击拒绝')
            action.click(res.rect.centerX(), res.rect.centerY())
            time.sleep(0.5)
        res = Selector().desc("Phone number").type("EditText").clickable(True).find()
        if res is not None:
            print(f'进入了输入手机号界面')
            set_proxy_main(phone, url, ip, port, user, password)
            time.sleep(0.5)
            return
        time.sleep(0.5)
        jc += 1


def main():
    info_path = R.sd()
    with open(info_path + '/info.txt', 'r') as f:
        info = f.readline()
    print(info)
    phone = info.split('----')[0]
    url = info.split('----')[1]
    ip = info.split('----')[2]
    port = info.split('----')[3]
    user = info.split('----')[4]
    password = info.split('----')[5]
    print(f'手机号：{phone}')
    print(f'url：{url}')
    print(f'ip：{ip}')
    print(f'port：{port}')
    print(f'user：{user}')
    print(f'password：{password}')
    login_account(phone, url, ip, port, user, password)