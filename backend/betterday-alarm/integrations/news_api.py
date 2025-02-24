import os
from newsapi import NewsApiClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variables
API_KEY = os.getenv("NEWSAPI_KEY")

if not API_KEY:
    raise ValueError("Missing NEWSAPI_KEY in .env file")

# Initialize NewsAPI client
newsapi = NewsApiClient(api_key=API_KEY)

def get_global_news():
    """Fetch the most important global news."""
    try:
        headlines = newsapi.get_top_headlines(
            language="en",
            page_size=5
        )
        articles = headlines.get("articles", [])
        
        return [
            f"{article['title']} - {article['source']['name']}"
            for article in articles
        ]
    except Exception as e:
        return [f"Error fetching global news: {str(e)}"]

if __name__ == "__main__":
    print("\nMost Important Global News:")
    print("\n".join(get_global_news()))
