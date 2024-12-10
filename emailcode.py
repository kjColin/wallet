import imaplib
import email
from email.header import decode_header
import re
import time

def email_code():
    # 邮箱配置
    username = "baibai5845203344@qq.com"
    password = "rjsmirfvvegwbcda"
    imap_server = "imap.qq.com"  # 替换为你的邮箱IMAP服务器

    try:
        # 连接到邮箱
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        mail.select("inbox")  # 选择收件箱

        time.sleep(10)  # 等待10秒，可以根据需要调整

        # 获取未读邮件的ID
        status, messages = mail.search(None, '(UNSEEN)')
        mail_ids = messages[0].split()

        if mail_ids:
            latest_email_id = mail_ids[-1]  # 最新未读邮件的ID

            # 获取最新未读邮件内容
            status, msg_data = mail.fetch(latest_email_id, '(RFC822)')
            msg = email.message_from_bytes(msg_data[0][1])

            # 检查发件人是否为 noreply
            from_ = msg.get("From")
            if "noreply" not in from_.lower():
                print("发件人不是 noreply，跳过此邮件。")
                return

            # 获取邮件内容
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/html":  # 确保获取HTML部分
                        body = part.get_payload(decode=True).decode()
            else:
                body = msg.get_payload(decode=True).decode()

            # 使用正则表达式提取验证码
            code_match = re.search(r'(\d{6})', body)
            if code_match:
                verification_code = code_match.group(1)
                print("验证码:", verification_code)
                return verification_code
            else:
                print("未找到验证码。")
        else:
            print("没有找到未读邮件。")

    except Exception as e:
        print("发生错误:", e)

    finally:
        # 关闭连接
        mail.logout()

email_code()