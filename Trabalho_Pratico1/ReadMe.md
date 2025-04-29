```markdown
# Trabalho Prático 1 - Processamento de Linguagem Natural em Engenharia Biomédica

Este repositório contém os materiais e scripts desenvolvidos no âmbito do **Trabalho Prático 1** da unidade curricular de **Processamento de Linguagem Natural em Engenharia Biomédica**, do Mestrado em Informática Médica.

## Objetivo

O objetivo principal deste projeto foi aplicar técnicas de **Processamento de Linguagem Natural (PLN)** para extrair e estruturar informação relevante a partir de documentos PDF da área biomédica, transformando dados não estruturados em **ficheiros JSON** organizados e reutilizáveis.

## Membros do Grupo

- Ana Beatriz Salgado Andrade - PG56107  
- Filipa José Rodrigues de Araújo Costa - PG56123  
- Leonor de Amorim Pereira - PG57813

## Orientação

- Luís Filipe Cunha  
- José João Almeida

---

## Estrutura do Projeto

### 1. [`diccionari-multilinguee-de-la-covid-19.pdf`](#)
- **Conversão para texto**: Utilização de script com PyMuPDF.
- **Limpeza e preparação**: Remoção de conteúdo irrelevante e normalização.
- **Extração e estruturação**: Organização dos conceitos em JSON com campos como designação, categoria, traduções, códigos, definições e notas.

### 2. [`m_glossario-tematico-monitoramento-e-avaliacao.pdf`](#)
- **Conversão para texto**: Leitura de blocos por cor e posição.
- **Limpeza integrada**: Filtragem por cor e tamanho, exclusão de ruído.
- **Extração com Python**: Segmentação por tipo, número, descrição, sinónimos, remissivas, equivalentes e notas.

### 3. [`glossario_neologismos_saude.pdf`](#)
- **Conversão para `.txt` e `.html`**: Para preservar marcas tipográficas.
- **Limpeza e integração**: Eliminação de HTML redundante, deteção de itálicos.
- **Extração com Python**: Mapeamento detalhado para JSON com campos como definição, sigla, equivalências, informação enciclopédica, abonações e marcas tipográficas.

---

## Tecnologias Utilizadas

- **Python 3**
- **PyMuPDF (fitz)** - Extração de texto de PDFs
- **Regex** - Extração estruturada de dados
- **JSON** - Armazenamento estruturado
- **pdftotext / pdftohtml** - Conversão de documentos

---

## Resultados

- Criação de três ficheiros `.json` com estrutura hierárquica e campos semânticos completos.
- Automatização de processos de extração e limpeza.
- Superação de diversos desafios técnicos (ex: inconsistências tipográficas, variações de formatação, ruído textual).

---

## Conclusão

O trabalho demonstrou a viabilidade e utilidade das técnicas aplicadas a documentos biomédicos, reforçando a importância de abordagens sistemáticas na engenharia de dados textuais. Os scripts desenvolvidos são reutilizáveis e podem ser aplicados a outros glossários semelhantes no futuro.

---
