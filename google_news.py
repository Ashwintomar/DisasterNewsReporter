import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_google_news():
    keywords = ["floods", "earthquakes", "tsunami", "deadly+fire", "hurricane", "tornado", "volcanic+eruption"]
    all_news_data = []

    for keyword in keywords:
        url = f"https://news.google.com/search?q={keyword}&hl=en-IN&gl=IN&ceid=IN%3Aen"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='IFHyqb DeXSAc')

        for i, article in enumerate(articles):
            if i >= 20:
                break

            title_element = article.find('a', class_='JtKRv')
            source_element = article.find('div', class_='vr1PYe')
            time_element = article.find('time', class_='hvbAAd')

            if title_element and source_element and time_element:
                all_news_data.append({
                    'Title': title_element.get_text(),
                    'Source': source_element.get_text(),
                    'Time': time_element.get_text(),
                    'Keyword': keyword
                })

    return all_news_data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    google_data = scrape_google_news()
    save_to_csv(google_data, 'google_news.csv')
    print(f"Scraped {len(google_data)} articles and saved to google_news.csv")
