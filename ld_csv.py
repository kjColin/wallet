import os
import time
import requests
import csv


class LD:
    # 注意修改模拟器路径
    # 模拟器控制类，用于管理和操作LDPlayer模拟器
    def __init__(self):
        self.ld_path = "E:\\leidian\\LDPlayer9\\dnconsole.exe"  # 配置模拟器列表

    # 启动指定索引的模拟器
    def start(self, index: int = 0):  # 模拟器的索引，第一个是0，第二个是1，以此类推
        cmd = f"{self.ld_path} launch --index {index}"
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result

    # 获取所有模拟器的详细信息
    # 包括索引，标题，顶层窗口句柄等信息
    def list2(self):
        cmd = f"{self.ld_path} list2"
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result

    # 创建一个新的模拟器
    def add(self):
        cmd = f"{self.ld_path} add"
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result

    # 修改指定索引的模拟器属性
    def modify(self, index: int = 0, w: int = 1080, h: int = 1920, dpi: int = 480, cpu: int = 4, memory: int = 4096,
               imei: str = 'auto', mac: str = 'auto', androidid: str = 'auto', simserial: str = 'auto'):
        cmd = (f"{self.ld_path} modify --index {index} --resolution {w},{h},{dpi} --cpu {cpu} --memory {memory}"
               f" --imei {imei} --mac {mac} --androidid {androidid} --simserial {simserial}")
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result

    # 关闭指定索引的模拟器
    def quit(self, index: int = 0):
        time.sleep(5)
        cmd = f"{self.ld_path} quit --index {index}"
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result

    # 关闭所有模拟器
    def quitall(self):
        time.sleep(5)
        cmd = f"{self.ld_path} quitall"
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result

    # 判断指定索引的模拟器是否正在运行
    def isrunning(self, index: int = 0):
        time.sleep(5)
        cmd = f"{self.ld_path} isrunning --index {index}"
        process = os.popen(cmd)
        result = process.read()
        process.close()
        print(result)
        if result == 'running':
            return True
        else:
            return False

    # 安装指定路径的apk文件到计算机上的模拟器
    # 下载apk
    def install_apk(self, index: int = 0, apk_path: str = None):
        time.sleep(5)
        cmd = f"{self.ld_path} --index {index} --action install --package {apk_path}"
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result

    # 复制指定索引的模拟器
    def copy(self, index: int = 0):
        '''
        【复制模拟器】
        :param name: 新模拟器标题
        :param index: 原模拟器序号
        :return: 控制台调试内容
        '''
        cmd = f"{self.ld_path} copy --from {index}"
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result

    # 移除指定索引的模拟器
    def remove(self, index: int = 0):
        '''
                【移除模拟器】
                :param index: 模拟器序号
                :return: 控制台调试内容
                '''
        cmd = f"{self.ld_path} remove --index {index}"
        process = os.popen(cmd)
        result = process.read()
        process.close()
        print(result)
        return result

    # 启动指定索引的模拟器中的指定包名应用
    def launchx(self, index: int = 0, packagename: str = None):
        time.sleep(5)
        cmd = f"{self.ld_path} launchex --index {index} --packagename {packagename}"
        process = os.popen(cmd)
        result = process.read()
        process.close()
        print(result)
        return result

    # 发送adb命令到指定索引的模拟器
    def send_adb_command(self, index: int = 0, command: str = None):
        time.sleep(1)

        cmd = f'{self.ld_path} adb --index {index} --command "{command}"'
        print(f'执行命令：{cmd}')
        process = os.popen(cmd)
        result = process.read()
        process.close()
        return result


# 读取账号信息并返回账号列表
import re


def get_accounts():
    account_list = []
    # 定义正则表达式模式，用于去掉头部和尾部的双引号和逗号
    pattern = re.compile(r'^"|",$')

    # 打开 account.csv 文件并读取每一行
    try:
        with open('account.csv', 'r', encoding='utf-8') as file:
            for line in file:
                # 去除首尾空白并用 '----' 分割行
                parts = line.strip().split('----')
                if len(parts) == 2:  # 确保分割后有两个部分
                    # 使用正则表达式去掉头部和尾部的双引号和逗号
                    phone = re.sub(pattern, '', parts[0])
                    url = re.sub(pattern, '', parts[1])

                    account_info = {
                        'phone': phone,  # 第一部分是 phone
                        'url': url  # 第二部分是 url
                    }
                    account_list.append(account_info)  # 将字典添加到列表中
            print(f'账号数量: {len(account_list)}')
    except FileNotFoundError:
        print("文件 account.csv 未找到。")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
    return account_list


# 读取代理信息并返回代理列表
def get_proxies():
    # 定义一个空列表，用于存储提取的数据
    proxies_list = []
    # 打开 proxies.txt 文件并读取每一行
    with open('proxies.txt', 'r') as file:
        for line in file:
            # 去除行末的换行符并按冒号分割
            parts = line.strip().split(':')
            # 确保分割出的部分有四个
            if len(parts) == 4:
                # 将提取的数据存储为字典
                proxy = {
                    'ip': parts[0],  # IP 地址
                    'port': parts[1],  # 端口号
                    'user': parts[2],  # 用户名
                    'password': parts[3]  # 密码
                }
                proxies_list.append(proxy)
        print(f'代理数量:{len(proxies_list)}')
        # 返回包含字典的列表
        return proxies_list
def wait_url():

    # 等待5s
    res_ = {}
    url = 'http://192.168.2.125:9096/api/model/get?name=wallet'
    while True:
        try:
            res_= requests.get(url).json()
            return res_
        except Exception as e:
            res_ = {}
        print('res_-->',res_)
        time.sleep(1)



def main():
    # 实例化 LD 类
    ld = LD()
    with open('account3.csv', 'r') as file:
        reader = csv.reader(file)
        for item in reader:
            phone=item[0].split('----')[0]
            url=item[0].split('----')[1]
            ip = item[1].split(':')[0]
            port = item[1].split(':')[1]
            user = item[1].split(':')[2]
            password = item[1].split(':')[3]

            print(f'开始创建模拟器')
            print(f'手机号：{phone}')
            print(f'url:{url}')
            print(f'代理IP：{ip}')
            print(f'代理port：{port}')
            print(f'代理user：{user}')
            print(f'代理password：{password}')

            # 存入数据文件
            with open('info.txt', 'w') as f:
                f.write(f'{phone}----{url}----{ip}----{port}----{user}----{password}\n')
                f.close()
            print(f'账号信息写入文件成功')
            # 复制模拟器
            ld.copy(1)
            # 等待5s
            time.sleep(5)
            # 读取最后一个模拟器
            test = ld.list2()
            res = ld.list2().strip()
            index = res.split('\n')[-1].split(',')[0]
            ld.modify(int(index))

            res = ld.start(int(index))
            # 等待5s
            time.sleep(5)
            res = ld.isrunning(int(index))
            print(f'模拟器是否在运行：{res}')
            if res:
                res = wait_url()
                if res.get('code') == 1:
                    # 发送 adb 命令
                    for i in range(10):
                        path = os.path.join(os.getcwd(), 'info.txt')
                        ld.send_adb_command(int(index), f"push {path} /sdcard/")
                        time.sleep(2)
                    # 脚本启动地址
                    script_url = 'http://192.168.2.125:9096/api/model/run?name=wallet'
                    res = requests.get(script_url)
                    print(res.text)
                    time.sleep(1)
            # 等待时间 结束后执行下一个号
            time.sleep(300)
            # 停止模拟器
            ld.quit(int(index))
            # 移除模拟器
            # return


if __name__ == '__main__':
    main()