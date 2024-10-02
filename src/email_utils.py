import smtplib
from email.mime.text import MIMEText
from .config import EMAIL_ADDRESS, EMAIL_AUTH_CODE, SMTP_SERVER, SMTP_PORT, RECIPIENT_EMAIL  # 使用相对导入

def send_alert_email(keyword, url):
    subject = '网页监测告警'
    body = f"在监测的页面 {url} 中检测到关键词: {keyword}"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    
    try:
        print(f"尝试连接到 SMTP 服务器: {SMTP_SERVER}:{SMTP_PORT}")
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            print("SMTP 服务器连接成功")
            print(f"尝试登录邮箱: {EMAIL_ADDRESS}")
            server.login(EMAIL_ADDRESS, EMAIL_AUTH_CODE)
            print("邮箱登录成功")
            print(f"正在发送邮件到: {RECIPIENT_EMAIL}")
            server.send_message(msg)
            print("告警邮件已发送")
    except Exception as e:
        print(f"发送邮件失败: {e}")
        print(f"SMTP_SERVER: {SMTP_SERVER}")
        print(f"SMTP_PORT: {SMTP_PORT}")
        print(f"EMAIL_ADDRESS: {EMAIL_ADDRESS}")
        print(f"RECIPIENT_EMAIL: {RECIPIENT_EMAIL}")
        # 不要打印 EMAIL_AUTH_CODE