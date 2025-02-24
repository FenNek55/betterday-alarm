import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def generate_good_morning_message(data_string):
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": f"Jesteś personalnym informatorem, wygeneruj wiadomość powitalną zaczynając od słów 'Dzień dobry Karol, pora wstawać!'. Następnie podaj najważniejsze wiadomości na podstawie przekazanych dalej nagłówków oraz podsumuj wydarzenia z mojego kalendarza na podstawie przekazanych dalej danych, jeśli ich nie ma to pomiń daną sekcję. Pod koniec wiadomości życz miłego dnia, nawiązując krótko o wydarzeniach z kalendarza. Pomiń wszelkie znaki specjalne w swojej wiadomości tak, by była przygotowana na użycie z narzędziem text-to-speech. Możesz przetłumaczyć anglojęzyczne teksty z kalendarza oraz wiadomości. {data_string}"}]}]
    }
    response = requests.post(GEMINI_URL, headers=headers, json=data)

    if response.status_code == 200:
        candidates = response.json().get("candidates", [])
        if candidates:
            parts = candidates[0].get("content", {}).get("parts", [])
            if parts:
                return parts[0].get("text", "No news available.")
    
    return "No news available at the moment."

if __name__ == "__main__":
    string = generate_good_morning_message("Calendar: 16:00 go for a walk 22:00 work on my app. News: S&P stocks drop 3%")
    print(string)