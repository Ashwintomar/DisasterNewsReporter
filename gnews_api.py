import json
import urllib.request
import pandas as pd
import time

def scrape_gnews_api():
    keywords = ["flood", "earthquake", "tsunami", "fire", "hurricane", "tornado", "volcano"]
    apikey = "d46c8c4c6a43ed9e2eb6933a0176226e"
    all_news_data = []

    for keyword in keywords:
        url = f"https://gnews.io/api/v4/search?q=indian+{keyword}&lang=en&country=in&max=20&apikey={apikey}"

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode("utf-8"))
            articles = data.get("articles", [])

            for article in articles:
                all_news_data.append({
                    'Title': article.get('title', 'No title'),
                    'Description': article.get('description', 'No description'),
                    'Source': article['source'].get('name', 'No source'),
                    'PublishedAt': article.get('publishedAt', 'No date'),
                    'Keyword': keyword
                })

        time.sleep(5)

    return all_news_data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    gnews_data = scrape_gnews_api()
    save_to_csv(gnews_data, 'gnews_api.csv')
    print(f"Scraped {len(gnews_data)} articles and saved to gnews_api.csv")
