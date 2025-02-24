import os
import vlc
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
RADIO_URL = os.getenv("RADIO_URL")

def play_radio():
    instance = vlc.Instance("--network-caching=1000")  # Increase network cache to 1000ms
    player = instance.media_player_new()
    media = instance.media_new(RADIO_URL)
    player.set_media(media)
    player.play()
    return player  # Return player to keep control

def play_radio_for_duration(duration_in_min):
    player = play_radio()

    try:
        time.sleep(duration_in_min * 60) 
    except KeyboardInterrupt:
        print("Stopping radio...")

    print("Stopping radio after 30 minutes...")
    player.stop()

if __name__ == "__main__":
    print("Playing radio for 1 minute...")
    play_radio_for_duration(1)
