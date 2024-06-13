import smtplib
import requests
import pytz
import os
from datetime import datetime
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
def capitalizy(input_string):
    return input_string.title()
def convert_tz(time):
    time = time.replace("Z", '')
    input_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
    source_timezone = pytz.utc
    timezone = "US/Central" # NOTE: change this to your local timezone like "Europe/Amsterdam" for more accurate datetime
    target_timezone = pytz.timezone(timezone)
    localized_datetime = source_timezone.localize(input_datetime)
    converted_datetime = localized_datetime.astimezone(target_timezone)
    date = converted_datetime.strftime("%B %dth, %A %Y at %I:%M %p")
    return date
channel_id = os.environ['channel_id']
api_key = os.environ['api_key'] # get an api key on the google cloud youtube data v3 api service; THIS IS A MUST!!
with requests.get(f'https://channel-updateapi.vercel.app/check?channel_id={channel_id}&api_key={api_key}') as app:
    aps = app.json()
    if aps['text'].startswith("No videos uploaded"):
        print("No video uploaded D:")
    elif aps['text'].startswith("Videos"):
        num = 0
        for video in aps['videos']:
            num += 1
            title = capitalizy(video['channel_title'])
            time = convert_tz(video['published'])
            print(f"\033[92mYay! {title} released {video['title']} on {time}\nWatch it here: {video['url']}\033[0m")
            try:
                sender_email = os.environ['email'] # this is your email. the one you used for your app password
                sender_password = os.environ['email_password'] # get a gmail app password (search up "gmail app password" to learn more)
                recipient_email = os.environ['email'] # sends to your email or the same email you used 
                subject = f"{title} released a new video!"
                message = f"{title} released {video['title']} on {time}\nWatch it here: {video['url']}"
                send_email(sender_email, sender_password, recipient_email, subject, message)
                print(f"Email Sent! \nEmail number {num}/{len(aps['videos']} {len(aps['videos']-num} more video(s)")
            except Exception as e:
                print(f"Error! an error occured sending the email...\n{e}")
                exit(-1)
    elif app.status_code == 400:
        print("Please provide a channel id and api key or valid channel ids and api keys :D")
        exit(-1)
    else:
        print(f"Oh no! the api has encountered an error! Please create an issue in the issue tab. Status code: \n{app.status_code}\n Error Text: \n{app.text}")
        exit(-1)
