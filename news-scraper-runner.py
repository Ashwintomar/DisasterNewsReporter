import os
import pandas as pd
from importlib import import_module

def import_module_from_file(module_name):
    try:
        return import_module(module_name)
    except ImportError:
        print(f"Error importing {module_name}. Make sure the file exists in the same directory.")
        return None

bing_news = import_module_from_file('bing_news')
google_news = import_module_from_file('google_news')
gnews_api = import_module_from_file('gnews_api')

def run_all_scrapers():
    if bing_news:
        bing_data = bing_news.scrape_bing_news()
        bing_news.save_to_csv(bing_data, 'bing_news.csv')
        print("Bing News data saved")

    if google_news:
        google_data = google_news.scrape_google_news()
        google_news.save_to_csv(google_data, 'google_news.csv')
        print("Google News data saved")

    if gnews_api:
        gnews_data = gnews_api.scrape_gnews_api()
        gnews_api.save_to_csv(gnews_data, 'gnews_api.csv')
        print("GNews API data saved")

def merge_csv_files():
    csv_files = ['bing_news.csv', 'google_news.csv', 'gnews_api.csv']
    dfs = []

    for file in csv_files:
        if os.path.exists(file):
            df = pd.read_csv(file)
            if file == 'bing_news.csv':
                df = df.rename(columns={'Snippet': 'Description'})
            elif file == 'google_news.csv':
                df = df.rename(columns={'Time': 'PublishedAt'})
                df['Description'] = ''  # Add empty Description column
            dfs.append(df)

    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        combined_df.to_csv('combined_news.csv', index=False)
        print("Combined news data saved to combined_news.csv")

        for file in csv_files:
            if os.path.exists(file):
                os.remove(file)
        print("Individual CSV files deleted")
    else:
        print("No data to combine. Make sure at least one scraper ran successfully.")

if __name__ == "__main__":
    run_all_scrapers()
    merge_csv_files()
    print("All tasks completed successfully")