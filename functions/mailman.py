import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import datetime

def send_email(person):
    load_dotenv()
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

    msg = EmailMessage()
    msg['Subject'] = f"Daily Covid Check {datetime.datetime.now().strftime('%m/%d/%y %I:%M %p')}"
    msg['From'] = EMAIL_ADDRESS 
    msg['BCC'] = person['email']
    
    with open(f'screenshots/{person["ratio"]}.png', 'rb') as png:
        msg.add_attachment(png.read(), maintype='application', subtype='octet-stream', filename=f'{person["device"]}.png')
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
        smtp.send_message(msg)