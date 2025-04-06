import requests
from bs4 import BeautifulSoup
import json
from bs4 import NavigableString


def doenca_info(url_href):
    url_doenca = 'https://www.atlasdasaude.pt' + url_href
    response = requests.get(url_doenca)
    
    if response.status_code != 200:
        return {"error": f"Erro ao acessar a URL {url_doenca}, código de status: {response.status_code}"}
    
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    div_content = soup.find("div", class_="node-doencas")
    if div_content is None:
        return {"error": "Não foi possível encontrar a div da doença."}

    data_div = div_content.find("div", class_="field-name-post-date")
    data_hora = data_div.div.text.strip() if data_div else "Data não disponível"

    
    content_div = div_content.find("div", class_="field-type-text-with-summary")
    if not content_div:
        return {"url": url_doenca, "date": data_hora, "content": {}}

    content_data = {
        "introducao": [],
        "causas": [],
        "sintomas": [],
        "tratamento": [],
        "artigos_relacionados": []
    }

    current_section = "introducao"
    field_item = content_div.find("div", class_="field-item")

    for element in field_item.children:
        if not element.name:
            continue

        if element.name == 'h2':
            text = element.get_text(strip=True).lower()
            if "causas" in text:
                current_section = "causas"
            elif "sintomas" in text:
                current_section = "sintomas"
            elif "tratamento" in text:
                current_section = "tratamento"
            elif "artigos relacionados" in text.lower():
                current_section = "artigos_relacionados"

        if element.name == 'p':
            content_data[current_section].append(element.get_text(strip=True))
        elif element.name == 'ul' and current_section == "sintomas":
            content_data[current_section] = [li.get_text(strip=True) for li in element.find_all('li')]
        elif element.name == 'h3' and current_section == "artigos_relacionados":
            link = element.find('a')
            if link:
                content_data[current_section].append({
                    "titulo": link.get_text(strip=True),
                    "url": link['href']
                })

    
    nota_div = div_content.find("div", class_="field-name-field-nota")
    nota = nota_div.get_text(strip=True) if nota_div else ""

    return {
        "url": url_doenca,
        "date": data_hora,
        "content": {
            "descricao": content_data["introducao"],
            "causas": content_data["causas"],
            "sintomas": content_data["sintomas"],
            "tratamento": content_data["tratamento"],
            "artigos_relacionados": content_data["artigos_relacionados"]
        },
        "nota": nota
    }


def doencas_letra(letra):
    url = 'https://www.atlasdasaude.pt/doencasaaz/' + letra
    print(url)
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": f"Erro ao acessar a URL {url}, código de status: {response.status_code}"}

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    doencas = {}
    for div_row in soup.find_all("div", class_="views-row"):
        h3 = div_row.div.h3 if div_row.div and div_row.div.h3 else None
        if h3 and h3.a:
            designacao = h3.a.text
            doenca_url = h3.a["href"]

            doenca_detalhes = doenca_info(doenca_url)

            desc_div = div_row.find("div", class_="views-field-body")
            desc = desc_div.div.text if desc_div else "Descrição não disponível"

            doenca_detalhes["resumo"] = desc.strip().replace(" ", " ")

            doencas[designacao] = doenca_detalhes

    return doencas


res = {}
for a in range(ord('a'), ord('z') + 1):
    letra = chr(a)
    print(f"Processando letra {letra.upper()}...")
    try:
        res.update(doencas_letra(letra))
    except Exception as e:
        print(f"Erro na letra {letra}: {e}")

with open("doencas_completo.json", "w", encoding="utf-8") as f_out:
    json.dump(res, f_out, indent=4, ensure_ascii=False)
