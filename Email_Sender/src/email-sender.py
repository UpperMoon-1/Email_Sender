'''
Created on Jan 16, 2025

@author: Giuseppe
'''

import os
from email.message import EmailMessage
import ssl
import smtplib



email_sender ='giuseppemuia2005@gmail.com'#my personal email
email_password=''#the 16 digit email password once you have turned on 2-step verification and started an app
email_receiver=''#email reciever


subject="Check this"#this is the subject of your email


#this is the body of your email
body="""
    This is sent by python
"""


em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject 
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender , email_receiver , em.as_string())





