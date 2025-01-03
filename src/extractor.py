 # Módulo para extrair o conteúdo completo das notícias


import requests
from bs4 import BeautifulSoup
from config import HEADERS


def extract_full_news(url):
    try:
        response = requests.get(url, headers=HEADERS, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            return '\n'.join(p.get_text() for p in paragraphs) or "Conteúdo não encontrado."
        return "Falha ao carregar o artigo."
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar o artigo: {e}"
