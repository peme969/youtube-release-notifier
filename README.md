<picture><img align="center" src="https://raw.githubusercontent.com/peme969/youtube-release-notifier/main/updater.webp" width="20%"/></picture>

# YouTube Video Release Notifier

### ⚡️ Latest video release notifier for YouTube

#### Powered by GitHub Actions 🐙 and Python 🐍

<p align="center">
  <a href="#feature">Feature</a>
  •
  <a href="#usage">Usage</a>     
  •
  <a href="#preview">Preview</a>
  •
</p>
<p align="center">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/peme969/youtube-release-notifier?style=flat">
  <img src="https://img.shields.io/github/forks/peme969/youtube-release-notifier?style=flat">
<p align="center">
  <img src="https://img.shields.io/github/stars/peme969/youtube-release-notifier?style=flat">
  <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/peme969/youtube-release-notifier?style=flat">
  <img src="https://img.shields.io/github/contributors/peme969/youtube-release-notifier?style=flat">
</p>
<p align="center">
  <a href="https://github.com/peme969/youtube-release-notifier/actions/workflows/daily.yml"><img src="https://github.com/peme969/youtube-release-notifier/actions/workflows/main.yml/badge.svg"></a>
  <a href="https://github.com/peme969/youtube-release-notifier/actions/workflows/manual.yml"><img src="https://github.com/peme969/youtube-release-notifier/actions/workflows/manual.yml/badge.svg"></a> (*)
</p>

#

### ⚠️ This repository is still in its early stages and may not work as expected... ⚠️
> [!IMPORTANT]
> **Read all** documents in this repo before doing anything!
> 
> Don't forget to star ⭐ this repository
> - Always update your repo following the original repo to get the latest update + bug fixes; I will not support anything if your repo is outdated
> - **Do not** enter your information ( token ) into 2 workflows file ( `main.yml` and `manual.yml` ) because it will not work and may leak your information to everyone
> - (*): Do not fork this repo if one of these or all of these ( not CodeQL ) GitHub Actions status badge show failing, and wait until one of these or two of these show passing then you can fork again
> - `Daily Release Detector` workflows always run every 14:00 UTC + 0; if you want to change it, refer to [this](https://github.com/gorouflex/DuoXPy/blob/main/README.md#how-to-change-the-schedule-that-the-workflows-will-run)
> <img src="https://i.imgur.com/htGeFlY.jpg">
  
# Feature 

- Sends to Mail with video url and publish date 🔥
- Accurately detects the latest video released every day ⚡

# Usage 

  1. Copy the youtube channel username (eg. https://youtube.com/channel/@Yarnhub -> Yarnhub)
  2. Go to [Youtube Channel ID Finder](https://www.streamweasels.com/tools/youtube-channel-id-and-user-id-convertor/) and paste the channel's username
  3. Convert it
  4. Copy the Youtube channel's ID
  5. [Fork this repository 🍴](https://github.com/peme969/youtube-release-notifier/fork)
  6. Go to your forked repository 🍴
  7. Go to `Settings > Secrets and Variables > Actions`, and click `New Repository secret`
  8. Use `channel_id` as the name and paste the channel id from Steps 4
  9. Add the email (name: email), email app password (name: email_password), channel id, and youtube data v3 api key (name: api_key)
  10. Go to your forked repository 🍴 and go to the Actions tab and press `I understand my workflows, go ahead and enable them`

> [!IMPORTANT]
> If you want to check manually, go to the [`Manual Release Checker`](https://github.com/peme969/youtube-release-notifier/blob/main/.github/workflows/manual.yml) workflows ( located in the Actions tab of the repo ). Then,enter the date you want to check (eg. 1).
> If you want to check another channel, enter the channel's id [use this to convert from username to channel id](https://www.streamweasels.com/tools/youtube-channel-id-and-user-id-convertor/). (this is optional)
> If you got `Oh no! the api encountered an error!` then create a bug in the issues tab (create it here not in your forked repo)!

<p align="center">
  ![image](https://github.com/peme969/youtube-release-notifier/assets/136040410/c8a5884f-064e-4286-9451-df3019eb6d40)
  ![image](https://github.com/peme969/youtube-release-notifier/assets/136040410/78734658-1b9a-4b81-8c72-b300eb143bf3)
  ![image](https://github.com/peme969/youtube-release-notifier/assets/136040410/5911658c-4865-47d8-83a9-e5e2a9e86a86)
</p>

## How to change the schedule that the workflows will run?

> [!IMPORTANT]
Daily workflow file path ( default is 14:00 UTC ± 0, and **DO NOT** enter your token here cause it will **not work** and may leak your information to everyone ): `.github/workflows/daily.yml`

- Well, GitHub uses UTC time ( UTC ± 0 ) for scheduling workflows, so we should convert it to our timezone

- For example: If I want to set the daily trigger to trigger at 9:00 PM ( UTC + 7 ) , I have to set it to 2:00 PM or 14:00 ( 24-hour format ) ( UTC ± 0 ) ( 2+7=9 ):

```
name: Daily Release Detector
on:
  schedule:
    - cron: '0 14 * * *' # <- Use UTC Time +0 , change your time here ( 14 is hour , 0 is minutes ) and use 24-hour format
```
- So, if I want the daily trigger to run at 5:00 AM ( UTC + 7 ), I have to set it to 10:00 PM ( UTC ± 0 ) ( use 24-hour format ):

```
name: Daily Release Detector
on:
  schedule:
    - cron: '0 22 * * *' # <- Use UTC Time +0 , change your time here ( 14 is hour , 0 is minutes ) and use 24-hour format
```


> [!NOTE]
> GitHub Actions schedules can sometimes be delayed by up to 15 minutes due to high demand, so don’t worry! ⏱️

# Preview

<p align="left">
  <img src="https://github.com/gorouflex/Sandy/blob/main/Img/DuoXPy/preview.png">
</p>
