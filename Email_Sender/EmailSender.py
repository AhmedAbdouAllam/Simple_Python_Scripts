import smtplib
from pathlib import Path
from email.message import EmailMessage
from string import Template
html=Path("mail.html").read_text()
html_string= Template(html)
# here you make your loop and condition over the database.


email= EmailMessage()
email['from']="Cairo University Training"
email['to']="kamelmohsenkamel@gmail.com"
email['subject']='Trial_Email'
email.set_content(html_string.substitute({ "CCE":"EEE" , "Google":"Allam"}),'html')
with smtplib.SMTP (host="smtp.gmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(Email,Password)
    smtp.send_message(email)
