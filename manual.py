import requests
import os
def convert(time):
  from datetime import datetime, timezone, timedelta
  input_datetime = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
  cst_offset = timedelta(hours=-6)
  cst_datetime = input_datetime.replace(tzinfo=timezone.utc) + cst_offset
  return cst_datetime.strftime("%Y-%m-%d %H:%M:%S")
days = os.environ['days']
with requests.get(f'https://yarnharb-detect.vercel.app/check?days={days}') as app:
  aps = app.json()
  if aps['text'] == "No video uploaded":
    print("No video uploaded D:")
  elif aps['text'].startswith("New video"):
    cst_time = convert(aps['published'])
    print(f"\033[92mYay! Yarnhub released {aps['title']} on {cst_time}\nWatch it here: {aps['url']}\033[0m")
  else:
    print(f"Oh no! the api has encountered an error! Status code: \n{app.status_code} Error: \n{app.text}")
