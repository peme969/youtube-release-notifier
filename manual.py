import requests
import pytz
from datetime import datetime
import os
def capitalizy(input_string):
    return input_string.title()
def convert_tz(time):
    time = time.replace("Z", '')
    input_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
    source_timezone = pytz.utc
    timezone = "US/Central"
    target_timezone = pytz.timezone(timezone)
    localized_datetime = source_timezone.localize(input_datetime)
    converted_datetime = localized_datetime.astimezone(target_timezone)
    date = converted_datetime.strftime("%B %dth, %A %Y at %I:%M %p")
    return date
days = os.environ['days']
channel_id = os.environ['channel_id']
api_key = os.environ['api_key']
with requests.get(f'https://channel-updateapi.vercel.app/check?channel_id={channel_id}&api_key={api_key}&days_ago={days}') as app:
    aps = app.json()
    if aps['text'].startswith("No videos uploaded"):
        print("No video uploaded D:")
    elif aps['text'].startswith("Videos"):
        for video in aps['videos']:
            title = capitalizy(video['channel_title'])
            formatted_datetime = convert_tz(video['published'])
            print(f"\033[92mYay! {title} released {video['title']} on {formatted_datetime}\nWatch it here: {video['url']}\033[0m")
    elif app.status_code == 400:
        print("Please provide a channel id and api key or valid channel ids and api keys :D")
        exit(-1)
    else:
        print(f"Oh no! the api has encountered an error! Please create an issue in the issue tab. Status code: \n{app.status_code}\nError text: \n{app.text}")
        exit(-1)
