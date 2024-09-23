import requests
from bs4 import BeautifulSoup
import csv

def scrape_bing_news():
    keywords = ["flood", "earthquake", "tsunami", "fire", "hurricane", "tornado", "volcano"]
    data = []

    for keyword in keywords:
        url = f"https://www.bing.com/news/search?q=recent+indian+{keyword}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to retrieve the page for {keyword}. Status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='news-card')

        for article in articles:
            title_element = article.find('a', class_='title')
            title = title_element.text.strip() if title_element else "No title"

            snippet_element = article.find('div', class_='snippet')
            snippet = snippet_element.text.strip() if snippet_element else "No snippet"

            source_element = article.find('div', class_='source')
            source = source_element.text.strip() if source_element else "No source"

            data.append([title, snippet, source, keyword])

    return data

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Snippet', 'Source', 'Keyword'])
        writer.writerows(data)

if __name__ == "__main__":
    bing_data = scrape_bing_news()
    save_to_csv(bing_data, 'bing_news.csv')
    print("Data has been successfully saved to bing_news.csv")
