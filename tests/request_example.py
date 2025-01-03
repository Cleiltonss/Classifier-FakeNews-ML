import requests
import json
import time
from bs4 import BeautifulSoup
import os

URL = "https://api.gdeltproject.org/api/v2/doc/doc?query=Brazil&mode=artlist&format=json&lang=Portuguese"
CACHE_FILE = 'news_cache.json'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
MAX_ATTEMPTS = 10
TIMEOUT = 10
MAX_RECORDS = 250  # Número máximo de artigos por requisição


# Requisição à API com paginação
def request_API(url, max_attempts=MAX_ATTEMPTS):
    all_articles = []
    seen_urls = set()  # Armazena URLs já coletadas
    offset = 0

    while True:
        paginated_url = f"{url}&maxRecords={MAX_RECORDS}&offset={offset}"
        attempt = 0

        while attempt < max_attempts:
            try:
                response = requests.get(paginated_url, headers=HEADERS, timeout=TIMEOUT)
                print(f'🔄 Tentativa {attempt + 1} - Status: {response.status_code} (Offset: {offset})')

                if response.status_code == 200:
                    data = response.json()
                    articles = data.get('articles', [])

                    if not articles:
                        print("🚫 Nenhuma notícia adicional encontrada.")
                        return {'articles': all_articles}

                    # Filtra artigos repetidos
                    new_articles = [a for a in articles if a['url'] not in seen_urls]
                    for article in new_articles:
                        seen_urls.add(article['url'])  # Adiciona URL ao conjunto
                        all_articles.append(article)

                    print(f"📄 {len(new_articles)} artigos únicos coletados no offset {offset}.")
                    offset += MAX_RECORDS

                    # Se não há novos artigos, encerra
                    if len(new_articles) == 0:
                        print("🚫 Todos os artigos já foram coletados. Encerrando...")
                        return {'articles': all_articles}

                    break
                elif response.status_code == 429:
                    print('⚠️ Muitas requisições (429). Aguardando 10 segundos...')
                    time.sleep(10)
                else:
                    print(f'❌ Erro na requisição: {response.status_code}')
                    break
            except requests.exceptions.RequestException as e:
                print(f'Erro de conexão: {e}')
            attempt += 1

        if attempt == max_attempts:
            print("🚫 Limite de tentativas atingido para o offset.")
            break

    return {'articles': all_articles}



# Função: Extrai o texto completo do artigo usando BeautifulSoup
def extract_article_content(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            return ' '.join(p.get_text() for p in paragraphs) or "🔸 Conteúdo não encontrado."
        return "❌ Falha ao carregar o artigo."
    except requests.exceptions.RequestException as e:
        return f"Erro ao acessar o artigo: {e}"


# Salva no cache (JSON)
def save_to_cache(data, file_path):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print("✅ Cache salvo com sucesso.")


# Carrega do cache (se existir)
def load_from_cache(file_path):
    if os.path.exists(file_path):
        print("♻️ Reutilizando dados do cache.")
        with open(file_path, "r") as f:
            return json.load(f)
    return None


# Função principal
def main():
    articles_data = request_API(URL)

    if not articles_data or 'articles' not in articles_data:
        print("🚫 Nenhum dado disponível.")
        return
    
    # Itera pelos artigos para extrair o conteúdo completo
    for article in articles_data.get('articles', []):
        print(f"\n🔹 {article['title']}\n🔗 {article['url']}")
        article['full_text'] = extract_article_content(article['url'])
        print(f"📝 {article['full_text'][:300]}...\n")

    # Salva em cache
    save_to_cache(articles_data, CACHE_FILE)


# Executa o script
if __name__ == "__main__":
    main()
