import os
import requests
from bs4 import BeautifulSoup
import time
import re

# Function to clean extracted text
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces/newlines
    text = re.sub(r'\[[0-9]*\]', '', text)  # Remove references (Wikipedia-style)
    return text.strip()

# Function to scrape articles from a list of URLs
def scrape_articles(category_folder, links_file, output_file):
    input_path = os.path.join(category_folder, links_file)
    output_path = os.path.join(category_folder, output_file)

    if not os.path.exists(input_path):
        print(f"[ERROR] {input_path} not found! Skipping...")
        return

    with open(input_path, "r", encoding="utf-8") as file:
        urls = file.readlines()

    scraped_texts = []

    for idx, url in enumerate(urls):
        url = url.strip()
        if not url:
            continue

        try:
            print(f"[{idx+1}/{len(urls)}] Scraping: {url}")
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code != 200:
                print(f"⚠️ Failed to fetch: {url} (Status {response.status_code})")
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            # Extracting text from <p> tags (modify this for different sites)
            paragraphs = soup.find_all("p")
            article_text = "\n".join([clean_text(p.get_text()) for p in paragraphs])

            if article_text:
                scraped_texts.append(article_text)
                time.sleep(1)  # Be nice to the server

        except Exception as e:
            print(f"⚠️ Error scraping {url}: {e}")
            continue

    # Save collected data
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(scraped_texts))

    print(f"✅ Saved scraped data to: {output_path} ({len(scraped_texts)} articles)")

"""    
# Example usage
category = "politics"  # Change this for each category
scrape_articles(f"data/{category}", "links.txt", f"{category}.txt")
"""


# Auto-detect all category folders inside "data/"
base_folder = "data"
categories = [f for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]

for category in categories:
    print(f"🚀 Processing Category: {category}")
    scrape_articles(os.path.join(base_folder, category), "links.txt", f"{category}.txt")
