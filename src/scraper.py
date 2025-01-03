# Módulo responsável por fazer scraping de notícias


import requests
import json
import urllib3
from config import URL, HEADERS
from tqdm import tqdm
from extractor import extract_full_news


def get_news(max_records):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
     
    paginated_url = f"{URL}&maxRecords={max_records}"
    collected_news = []
    try:
        response = requests.get(paginated_url, headers=HEADERS, verify=False)
        if response.status_code == 200:
            data = response.json()
            news = data.get('articles', [])
            
            if not news:
                print("⚠️ Nenhum artigo retornado pela API.")
            
            for article in tqdm(news, desc="Carregando notícias", unit=" notícia"):
                title = article.get('title', 'Sem Título')
                url = article.get('url', '#')
                content = extract_full_news(url)
                collected_news.append({
                    'title': title,
                    'content': content if content else "Conteúdo não encontrado.",
                    'url': url
                })
            
            with open('data/news.json', 'w', encoding='utf-8') as f:
                json.dump(collected_news, f, ensure_ascii=False, indent=4)
                print("\n✅ Artigos salvos em 'data/news.json'.")
        else:
            print(f"❌ Erro na requisição: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
