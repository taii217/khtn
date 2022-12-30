import os
from dotenv import load_dotenv

load_dotenv()

MIN_SALT = int(os.getenv('MIN_SALT', default='200'))
MAX_SALT = int(os.getenv('MAX_SALT',default='400'))

SMTP_MAIL = os.getenv('SMTP_MAIL', default='400')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', default='400')
SMTP_BACKEND = os.getenv('SMTP_BACKEND', default='smtp.gmail.com')





