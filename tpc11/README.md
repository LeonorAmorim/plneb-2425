
# Extrator de Artigos da Revista Portuguesa de Medicina Interna (RPMI)

Este script em Python tem como objetivo automatizar a extração de informações bibliográficas de artigos científicos publicados numa edição específica da [Revista Portuguesa de Medicina Interna (RPMI)](https://revista.spmi.pt). O resultado é um ficheiro JSON com os metadados dos artigos: título, resumo (abstract), DOI e data de publicação.

## Requisitos

- Bibliotecas:
  - `requests`
  - `beautifulsoup4`


## 🔍 Procuras Realizadas no HTML

Durante a extração, o script faz as seguintes procuras específicas no HTML de cada artigo:

- **Título do artigo**: Procurado no seletor `h1.page_title`.
- **Resumo (abstract)**: Procurado dentro da secção `section.item.abstract`, reunindo todos os parágrafos (`<p>`).
- **DOI**: Procurado no seletor `section.item.doi span.value a`.
- **Data de publicação**: Procurada no seletor `div.item.published div.value span`.

Além disso, a lista de links dos artigos é obtida através do seletor `h3.title a` na página principal da edição.

## Estrutura do JSON gerado

Cada entrada no JSON terá o seguinte formato:

```json
{
    "titulo": "Título do artigo",
    "abstract": "Resumo do artigo...",
    "doi": "https://doi.org/...",
    "data_publicacao": "2024-12-01"
}
```

## Ficheiro gerado

- `artigos_rpmi.json` – Contém todos os metadados dos artigos extraídos.
