import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email(sender_email, sender_password, recipient_email, subject, message):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
def convert(time):
  from datetime import datetime, timezone, timedelta
  input_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
  cst_offset = timedelta(hours=-6)
  cst_datetime = input_datetime.replace(tzinfo=timezone.utc) + cst_offset
  return cst_datetime.strftime("%Y-%m-%d %H:%M:%S")
with requests.get('https://yarnharb-detect.vercel.app/check') as app:
  aps = app.json()
  if aps['text'] == "No video uploaded":
    print("No video uploaded D:")
  elif aps['text'].startswith("New video"):
    cst_time = convert(aps['published'])
    print(f"\033[92mYay! Yarnhub released {aps['title']} on {cst_time}\nWatch it here: {aps['url']}\033[0m")
    try:
      sender_email = "mrcoderpeme@gmail.com"
      sender_password = "wewg phhy oxsn urip"
      recipient_email = "mrcoderpeme@gmail.com"
      subject = "Yarnhub released a new video!"
      message = f"Yarnhub released {aps['title']} on {cst_time}\nWatch it here: {aps['url']}"
      send_email(sender_email, sender_password, recipient_email, subject, message)
      print("Email Sent!")
    except Exception as e:
      print(f"Error! an error occured sending the email...\n{e}")
      exit(-1)
  else:
    print(f"Oh no! the api has encounreted an error! Status code: \n{app.status_code} Error: \n{app.text}")
