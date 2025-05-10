import requests
from bs4 import BeautifulSoup
import json

# URL da edição
url_base = "https://revista.spmi.pt"
url_edicao = f"{url_base}/index.php/rpmi/issue/view/135"

# Requisição da página da edição
response = requests.get(url_edicao)
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar links dos artigos
artigos_links = [a['href'] for a in soup.select('h3.title a')]

dados_artigos = []

for link in artigos_links:
    artigo_url = link if link.startswith("http") else f"{url_base}{link}"
    artigo_resp = requests.get(artigo_url)
    artigo_soup = BeautifulSoup(artigo_resp.text, "html.parser")

    # Título
    titulo_tag = artigo_soup.select_one('h1.page_title')
    titulo = titulo_tag.text.strip() if titulo_tag else ""

    # Abstract
    abstract_secao = artigo_soup.select_one('section.item.abstract')
    if abstract_secao:
        paragrafos = abstract_secao.find_all('p')
        abstract = "\n".join(p.text.strip() for p in paragrafos)
    else:
        abstract = ""

    # DOI
    doi_tag = artigo_soup.select_one('section.item.doi span.value a')
    doi = doi_tag.text.strip() if doi_tag else ""


    # Data de publicação
    data_tag = artigo_soup.select_one('div.item.published div.value span')
    data_publicacao = data_tag.text.strip() if data_tag else ""

    # Adicionar ao JSON
    dados_artigos.append({
        "titulo": titulo,
        "abstract": abstract,
        "doi": doi,
        "data_publicacao": data_publicacao
    })

# Guardar num ficheiro JSON
with open("artigos_rpmi.json", "w", encoding="utf-8") as f:
    json.dump(dados_artigos, f, ensure_ascii=False, indent=4)

print(f"{len(dados_artigos)} artigos extraídos com sucesso!")