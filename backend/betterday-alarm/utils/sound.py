import vlc
from mutagen.mp3 import MP3
import time
import os

def get_audio_duration(file_path):
    try:
        audio = MP3(file_path)
        return audio.info.length  # Returns duration in seconds
    except Exception as e:
        print(f"Could not determine duration of {file_path}: {e}")
        return 10  # Default fallback
    
def play_sound(file_path):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(file_path)
    player.set_media(media)
    player.play()

    time.sleep(get_audio_duration(file_path))
    player.stop()

if __name__ == "__main__":
    alarm_path = os.path.join(os.path.dirname(__file__), "..", "sounds", "alarm.mp3")
    print("Playing alarm sound...")
    play_sound(alarm_path)
