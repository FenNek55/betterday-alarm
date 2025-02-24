from integrations import google_calendar, news_api
from utils import text_to_speech, sound, radio
from llm import gemini
import os

def get_integrations_data():
    # Get news from both sources
    global_news = news_api.get_global_news()

    # Get calendar events
    calendar_events = google_calendar.get_upcoming_events()

    # Build the output string
    output = []
    
    output.append("\nLatest global news:")
    output.extend(global_news)
    
    output.append("\nCalendar entries for today:")
    if calendar_events:
        output.extend(calendar_events)
    else:
        output.append("No events scheduled for today")

    return "\n".join(output)

def generate_morning_message_audio():
    integrations_data = get_integrations_data()
    message_text = gemini.generate_good_morning_message(integrations_data)
    text_to_speech.generate_speech(message_text)

if __name__ == "__main__":
    print("Playing alarm sound...")
    sound.play_sound(os.path.join(os.path.dirname(__file__), "sounds", "alarm.mp3"))
    print("Generating morning message audio...")
    generate_morning_message_audio()
    print("Morning message audio generated successfully!")
    print("Playing morning message")
    sound.play_sound(os.path.join(os.path.dirname(__file__), "sounds", "generated_text.mp3"))
    print("Playing radio")
    radio.play_radio_for_duration(30)
