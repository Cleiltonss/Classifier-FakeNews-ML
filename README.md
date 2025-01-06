# Classifier-FakeNews-ML

## Descrição do Projeto
Classifier-FakeNews-ML é um projeto para coletar e extrair notícias de fontes online utilizando a API GDELT. O objetivo é desenvolver um classificador que, futuramente, possa distinguir entre notícias verdadeiras e falsas, utilizando técnicas de scraping, extração de texto e machine learning.

A arquitetura do projeto é modular, o que facilita a manutenção, a escalabilidade e o desenvolvimento contínuo.

---

## Estrutura do Projeto

```
Classifier-FakeNews-ML/
│
├── src/
│   ├── main.py                        # Script principal que orquestra o processo de scraping
│   ├── scraper.py                     # Módulo responsável por coletar notícias da API GDELT
│   ├── extractor.py                   # Função para extrair o conteúdo completo das notícias
│   ├── config.py                      # Configurações globais (URLs, headers, limites)
│   └── utils/
│       └── bar_progress.py            # Barra de progresso para exibir o carregamento no terminal
│
├── tests/                             # Testes unitários e de integração
│   ├── test_scraper.py                # Testes para o módulo scraper.py
│   ├── test_extractor.py              # Testes para o módulo extractor.py
│   └── test_utils.py                  # Testes para utilitários
│
├── data/                              # Armazena arquivos JSON de notícias
│   └── news.json                      # Arquivo com as notícias coletadas
│
├── references/                        # Materiais de referência e guias
│
├── env/                               # Ambiente virtual
│
├── requirements.txt                   # Dependências do projeto
├── README.md                          # Documentação do projeto
└── .gitignore                         # Arquivos e pastas a serem ignorados pelo Git
```

---

## Lógica e Funções de Cada Arquivo

### 1. **src/main.py**
- Arquivo principal que inicia o processo de scraping.
- Importa o módulo `scraper` e executa a coleta de notícias com base na configuração `MAX_RECORDS` do arquivo `config.py`.

**Exemplo de execução:**
```python
from scraper import get_news
from config import MAX_RECORDS

if __name__ == "__main__":
    get_news(MAX_RECORDS)
```

---

### 2. **src/scraper.py**
- Realiza a requisição de notícias da API GDELT.
- Itera sobre os artigos retornados e extrai o conteúdo completo utilizando a função `extract_full_news` do módulo `extractor.py`.
- Salva os dados em formato JSON no diretório `data/`.
- Utiliza `tqdm` para mostrar o progresso do scraping.

---

### 3. **src/extractor.py**
- Contém a função `extract_full_news` que recebe uma URL e realiza scraping no site da notícia.
- Utiliza `BeautifulSoup` para extrair o texto completo da notícia a partir das tags `<p>`.

---

### 4. **src/config.py**
- Define configurações globais para o projeto.
- Inclui a URL base da API GDELT, headers HTTP e o número máximo de registros a serem coletados.

---

### 5. **src/utils/bar_progress.py**
- Função para exibir a barra de progresso durante o scraping.
- Utiliza a biblioteca `tqdm` para melhorar a experiência do usuário no terminal.

**Exemplo de uso:**
```python
from tqdm import tqdm

def show_progress(iterable, description):
    return tqdm(iterable, desc=description, unit=" notícia")
```

---

## Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/usuario/Classifier-FakeNews-ML.git
```
2. Acesse o diretório do projeto:
```bash
cd Classifier-FakeNews-ML
```
3. Crie e ative o ambiente virtual:
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate    # Windows
```
4. Instale as dependências:
```bash
pip install -r requirements.txt
```
5. Execute o projeto:
```bash
python src/main.py
```

---

## Testes
- Os testes estão localizados na pasta `tests/` e cobrem as principais funções do projeto.
- Para executar todos os testes:
```bash
pytest tests/
```

---

## Contribuição
Contribuições são bem-vindas! Para contribuir:
1. Crie um fork do projeto.
2. Crie uma branch para sua nova feature (`git checkout -b feature/nova-feature`).
3. Faça commit das mudanças (`git commit -m 'Adiciona nova feature'`).
4. Envie para o branch principal (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## Licença
MIT License