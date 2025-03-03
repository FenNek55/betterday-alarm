# Alarm App

## Overview
This project is an alarm system that plays an alarm sound, fetches news headlines, and personalizes a morning message using an LLM. It integrates with Google Calendar to fetch daily events and provides customizable settings for alarm sounds and radio streams.

## Setup Instructions

### 1. Google Cloud Project Setup
To enable Google Calendar API access, create a google cloud project with IAM service role that has access to read your calendar (id is usually usesrs email address). In Gmail app you also need to share the calendar with the service role account.

### 2. Install Dependencies
Ensure you have Python installed, then install the required dependencies (ideally in virtual environment):
```sh
pip install -r requirements.txt
```

### 3. Create `.env` File
Create a `.env` file in the root directory based on `.env.example`:
```sh
GCLOUD_SERVICE_KEY=""
NEWSAPI_KEY=""
RADIO_URL=""
GEMINI_API_KEY=""
CALENDAR_ID=""
```
- `GCLOUD_SERVICE_KEY`: Stringified JSON Google Cloud service account key with access to read users calendar.
- `NEWSAPI_KEY`: API key for fetching news, free from NEWSAPI.
- `RADIO_URL`: URL of an online radio stream (must end with `.mp3`).
- `GEMINI_API_KEY`: API key for the Gemini LLM, free tier is enough.
- `CALENDAR_ID`: Google Calendar ID (usually your email address).

### 4. Change Alarm Sound
To customize the alarm sound, replace `alarm.mp3` in the project directory with your preferred audio file.

### 5. Set Radio Stream
The app supports radio streams from `https://ic2.smcdn.pl/` ending with `.mp3` (e.g., `https://ic2.smcdn.pl/2380-1.aac`). Set the desired radio URL in the `.env` file under `RADIO_URL`.

### 6. Personalize the Morning Message
To modify the personalized morning message, edit `gemini.py`. The prompt inside this file determines how the message is generated. Customize it to your preference.

## Running the App
After completing the setup, run the alarm program with:
```sh
python main.py
```
This will trigger alarms based on the configured schedule and personalize your morning experience. You can schedule it by setting a cron job for a given time.

## License
Do whatever you want with it.

