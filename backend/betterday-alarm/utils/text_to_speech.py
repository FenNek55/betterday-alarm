from gtts import gTTS
import os

def generate_speech(text):
    tts = gTTS(text=text, lang="pl")
    tts.save(os.path.join(os.path.dirname(__file__), "..", "sounds", "generated_text.mp3"))


if __name__ == "__main__":
    sample_text = "Dzień dobry! To jest przykładowy tekst do konwersji na mowę."
    print("Converting sample text to speech...")
    generate_speech(sample_text)
    print("Speech file generated at: sounds/generated_text.mp3")
