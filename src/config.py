import os
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件

# 从环境变量中读取邮箱配置信息
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_AUTH_CODE = os.getenv('EMAIL_PASSWORD')  # 使用授权码
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT', 465))  # 使用465端口，因为我们使用SMTP_SSL
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL', 'cdutboy928@gmail.com')

# 打印配置信息（不包括授权码）
print(f"邮箱配置: {EMAIL_ADDRESS}, {SMTP_SERVER}:{SMTP_PORT}, 接收者: {RECIPIENT_EMAIL}")