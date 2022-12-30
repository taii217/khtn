from email.mime.text import MIMEText
from random import randint
import smtplib
import ssl
from settings import SMTP_MAIL, SMTP_PASSWORD, SMTP_BACKEND
from email.mime.multipart import MIMEMultipart

port = 465  # For SSL
# Create a secure SSL context
context = ssl.create_default_context()


def random_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

    

def send_otp(receivers):
    print('Đang gửi otp đến email đăng nhập...')
    with smtplib.SMTP_SSL(SMTP_BACKEND, port, context=context) as server:
        otp = random_digits(6)
        text = f"Đây là mã otp để mã hoá, vui lòng không chia sẻ cho ai khác: {otp}"

        server.login(SMTP_MAIL, SMTP_PASSWORD)
        msg = MIMEMultipart()

        msg['From'] = SMTP_MAIL
        msg['To'] = receivers
        msg['Subject'] = 'OTP FROM GROUP SECURITY'
        message = MIMEText(text, "plain")
        msg.attach(message)

        server.send_message(msg)
        del msg
        print('Đã gửi otp đến email đăng nhập...')
        return otp


def check_otp(email):
    for i in range(3):
        otp = send_otp(email)
        if otp != int(input('OTP (đã gửi đến email của bạn): ')):
            print(f'otp thất bại ({i+1}/3)')
        else:
            return True
    return False


