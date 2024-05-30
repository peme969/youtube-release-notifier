import requests
import smtplib
import os
import pytz
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
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
def capitalizy(input_string):
    return input_string.title()    
def convert(time_24hr):
  hours, minutes = map(int, time_24hr.split(':'))
  period = "AM" if hours < 12 else "PM"
  hours = hours % 12
  if hours == 0:
      hours = 12
  time_12hr = f"{hours}:{minutes:02d} {period}"
  return time_12hr 
def convert_tz(time):
  input_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
  source_timezone = pytz.utc
  timesf = "US/Central"  # your timezone (make sure to edit it); it should look like this: US/Central or Europe/Amsterdam
  target_timezone = pytz.timezone(timesf)
  localized_datetime = source_timezone.localize(input_datetime)
  converted_datetime = localized_datetime.astimezone(target_timezone)
  return converted_datetime.strftime("%Y-%m-%d"),converted_datetime.strftime("%H:%M")
channel_id = os.environ['channel_id']
api_key = os.environ['api_key'] # get an api key on the google cloud youtube data v3 api service; THIS IS A MUST!!
with requests.get(f'https://channel-update-api.vercel.app/check?channel_id={channel_id}&api_key={api_key}') as app:
    aps = app.json()
    if aps['text'] == "No video uploaded":
        print("No video uploaded D:")
    elif aps['text'].startswith("New video"):
        title = capitalizy(aps['channel_title'])
        year,hour_minute = convert(aps['published'])
        print(f"\033[92mYay! {title} released {aps['title']} on {cst_time}\nWatch it here: {aps['url']}\033[0m")
        try:
            sender_email = os.environ['email'] # this is your email. the one you used for your app password
            sender_password = os.environ['email_password'] # get a gmail app password (search up "gmail app password" to learn more)
            recipient_email = os.environ['email'] # sends to your email or the same email you used for your app password
            subject = f"{title} released a new video!"
            message = f"{title} released at {convert(spec)} on {gen}\nWatch it here: {aps['url']}"
            send_email(sender_email, sender_password, recipient_email, subject, message)
            print("Email Sent!")
        except Exception as e:
            print(f"Error! an error occured sending the email...\n{e}")
            exit(-1)
    elif app.status_code == 400:
        print("Please provide a channel id and api key or valid channel ids and api keys :D")
        exit(-1)
    else:
        print(f"Oh no! the api has encountered an error! Please create an issue in the issue tab. Status code: \n{app.status_code} Error: \n{app.text}")
        exit(-1)
