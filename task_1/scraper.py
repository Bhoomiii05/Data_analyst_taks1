import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Website URL
url = "https://quotes.toscrape.com"

# Step 2: Get HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract data
quotes = []
authors = []
tags_list = []

for quote in soup.find_all('div', class_='quote'):
    quote_text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

    quotes.append(quote_text)
    authors.append(author)
    tags_list.append(", ".join(tags))

# Step 4: Save to CSV
df = pd.DataFrame({
    'Quote': quotes,
    'Author': authors,
    'Tags': tags_list
})

df.to_csv('quotes_dataset.csv', index=False)
print("✅ Done! quotes_dataset.csv saved.")
