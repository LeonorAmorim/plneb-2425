## Descrição

Este projeto teve como objetivo a extração de informações detalhadas sobre doenças a partir do site "Atlas da Saúde". O código recolhe dados de várias páginas de doenças, organiza-os e armazena-os em um arquivo JSON estruturado. As informações coletadas incluem a descrição, causas, sintomas, tratamentos, artigos relacionados e notas adicionais de cada doença.

## Funcionalidades

O código possui duas funções principais:

1. **doenca_info(url_href)**: Recolhe informações detalhadas de uma doença a partir de uma URL fornecida. As informações incluem a data de publicação, descrição, causas, sintomas, tratamentos, artigos relacionados e nota adicional.

2. **doencas_letra(letra)**: Recolhe as doenças que começam com uma determinada letra (A-Z) a partir de uma página de lista do site, processando cada doença individualmente e chamando a função `doenca_info` para extrair dados específicos.

Além disso, o código percorre todas as letras do alfabeto, recolhendo informações sobre doenças que começam com cada letra e armazena esses dados num arquivo JSON chamado `doencas_completo.json`.

## Bibliotecas Python:
  - `requests`: Para realizar as requisições HTTP.
  - `BeautifulSoup` (do pacote `bs4`): Para fazer parsing do conteúdo HTML.
  - `json`: Para manipulação de arquivos JSON.

