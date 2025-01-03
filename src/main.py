# Script principal que inicia o processo


from scraper import get_news
from config import MAX_RECORDS

if __name__ == "__main__":
    get_news(MAX_RECORDS)
