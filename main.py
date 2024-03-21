import requests
import smtplib
import os
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
def convert(time):
    input_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    source_timezone = pytz.utc
    timesf = os.environ['timezone'] # your timezone from the github secrets (make sure to add it)
    target_timezone = pytz.timezone(timesf)
    localized_datetime = source_timezone.localize(input_datetime)
    cdt_datetime = localized_datetime.astimezone(target_timezone)
    return cdt_datetime.strftime("%Y-%m-%d %H:%M:%S")
days = os.environ['days']
channel_id = os.environ['channel_id']
api_key = os.environ['api_key'] # get an api key on the google cloud youtube data v3 api service
with requests.get(f'https://channel-update-api.vercel.app/check?days={days}&channel_id={channel_id}&api_key={api_key}') as app:
    aps = app.json()
    if aps['text'] == "No video uploaded":
        print("No video uploaded D:")
    elif aps['text'].startswith("New video"):
        title = capitalizy(aps['channel_title'])
        cst_time = convert(aps['published'])
        print(f"\033[92mYay! {title} released {aps['title']} on {cst_time}\nWatch it here: {aps['url']}\033[0m")
        try:
            sender_email = os.environ['email']
            sender_password = os.environ['email_password']
            recipient_email = os.environ['email'] # sends to your email
            subject = f"{title} released a new video!"
            message = f"{title} released {aps['title']} on {cst_time}\nWatch it here: {aps['url']}"
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
