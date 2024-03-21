import requests
import os
from datetime import datetime, timezone, timedelta

def capitalizy(input_string):
    return input_string.title()

def convert(time):
    input_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
    cst_offset = timedelta(hours=-6)
    cst_datetime = input_datetime.replace(tzinfo=timezone.utc) + cst_offset
    return cst_datetime.strftime("%Y-%m-%d %H:%M:%S")

days = os.environ['days']
channel_id = os.environ['channel_id']
api_key = os.environ['api_key'] 

url = f'https://channel-update-api.vercel.app/check?days={days}&channel_id={channel_id}&api_key={api_key}'

response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
        if data['text'] == "No video uploaded":
            print("No video uploaded D:")
        elif data['text'].startswith("New video"):
            cst_time = convert(data['published'])
            title = capitalizy(data['channel_title'])
            print(f"\033[92mYay! {title} released {data['title']} on {cst_time}\nWatch it here: {data['url']}\033[0m")
    except ValueError:
        print("Error: Invalid JSON response.")
        print(response.text)
        exit(-1)
else:
    print(response.text, f"Status code: {response.status_code}")
    exit(-1)

