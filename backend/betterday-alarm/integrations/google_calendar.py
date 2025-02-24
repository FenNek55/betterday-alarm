import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
GCLOUD_SERVICE_KEY = os.getenv("GCLOUD_SERVICE_KEY")
CALENDAR_ID = os.getenv("CALENDAR_ID")

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def get_calendar_service():
    """Authenticate and return a Google Calendar API service object."""
    creds = service_account.Credentials.from_service_account_info(
        json.loads(GCLOUD_SERVICE_KEY), scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=creds)
    return service

def get_upcoming_events():
    """Fetch upcoming events from the primary calendar."""
    service = get_calendar_service()
    
    today = datetime.datetime.now(datetime.UTC)
    start_of_day = datetime.datetime.combine(today, datetime.time.min).isoformat() + "Z"
    end_of_day = datetime.datetime.combine(today, datetime.time.max).isoformat() + "Z"
    events_result = service.events().list(
        calendarId=CALENDAR_ID,  # Replace with your calendar ID
        timeMin=start_of_day,
        timeMax=end_of_day,
        singleEvents=True,
        orderBy="startTime",
    ).execute()
    
    events = events_result.get("items", [])
    
    if not events:
        print("No upcoming events found.")
        return []

    event_list = []
    for event in events:
        start = event["start"].get("dateTime", event["start"].get("date"))
        event_list.append(f"{start} - {event['summary']}")
    
    return event_list

if __name__ == "__main__":
    events = get_upcoming_events()
    print("\nUpcoming Events:")
    print("\n".join(events))