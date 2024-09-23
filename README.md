---

# 🌪️ Disaster News Reporter

![Python](https://img.shields.io/badge/Python-3.x-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Issues](https://img.shields.io/github/issues/Ashwintomar/DisasterNewsReporter)

Welcome to the **Disaster News Reporter** repository! This project scrapes news articles related to natural disasters, summarizes them using a Large Language Model (LLM), and categorizes them by keywords. The final output is a DOCX file with bullet points for each disaster category.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Installation](#-installation)
- [Usage](#-usage)
- [Scrapers](#-scrapers)
- [Summarization](#-summarization)
- [Output](#-output)
- [Contact](#-contact)

---

## 📝 Overview

**Disaster News Reporter** consists of Python scripts that perform the following tasks:

1. **Scrape** news articles from Bing, Google, and the GNews API.
2. **Merge** the scraped data into a single CSV file.
3. **Summarize** the news articles using a pre-trained Large Language Model (LLM) from Hugging Face Transformers.
4. **Categorize** the summarized bullet points by keywords (e.g., "flood", "earthquake", "tsunami").
5. **Save** the categorized bullet points into a DOCX file.

---

## ⚙️ Installation

To set up the project, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Ashwintomar/DisasterNewsReporter.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd DisasterNewsReporter
    ```

3. **Install the required libraries:**

    ```bash
    !pip install transformers torch beautifulsoup4 requests pandas python-docx
    ```

---

## 🚀 Usage

To run the project, execute the following command:

```bash
python news-scraper-runner.py
```

This will run all the scrapers, merge the data, summarize the articles, and generate the final DOCX file.

---

## 🕵️ Scrapers

The project includes three scrapers:

- **Bing News Scraper**: Scrapes news articles from Bing News.
- **Google News Scraper**: Scrapes news articles from Google News.
- **GNews API Scraper**: Fetches news articles using the GNews API.

Each scraper retrieves recent news articles related to natural disasters.

---

## 🧠 Summarization

The summarization process uses the `facebook/bart-large-cnn` model from Hugging Face Transformers. This pre-trained Large Language Model (LLM) generates concise summaries from longer texts, which are then split into bullet points.

**Model Used**: `facebook/bart-large-cnn`

---

## 📂 Output

The final output is a DOCX file named `summarized_news.docx`. This file contains bullet points categorized by keywords such as "flood", "earthquake", "tsunami", etc.

---

## 📬 Contact

For questions or feedback, feel free to contact:

- **Email**: [ashwintomar04@gmail.com](mailto:ashwintomar04@gmail.com)

Thank you for using the Disaster News Reporter!

---
