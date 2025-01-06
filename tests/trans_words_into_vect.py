# Transforming words into feature vectors
import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import re


count = CountVectorizer()


# Import JSON file of news(
with open('data/news.json', 'r', encoding='utf-8') as f: news_data = json.load(f)

# Split in arrays
titles = [item['title'] for item in news_data if 'title' in  item]
contents = [item['content'] for item in news_data if 'content' in item]

# # Bag words model
# bag_titles = count.fit_transform(titles)
# bag_contents = count.fit_transform(contents)

print(titles[3])

# Cleaning text data
def preprocessor(text):
    text = re.sub('<[^>]*>', '', text)

