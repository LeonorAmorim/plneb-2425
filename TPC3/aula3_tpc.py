import re

with open("dicionario_medico.txt", encoding='UTF-8') as file:
    texto = file.read()


texto = re.sub(r'\n\n(?!\f)', '\n\n@', texto)

texto= re.sub(r'\f','',texto)

def limpa_descricao(descricao):
    descricao = re.sub(r'@', '', descricao)
    return re.sub(r'\s+', ' ', descricao.strip()) 

conceitos_raw=re.findall(r'@(.*)\n([^@]*)', texto)
conceitos = [(designacao, limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]


def gera_html(conceitos):
    html_header = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8"/>
    </head>
    <body>
        <h3>Dicionário de conceitos Médicos</h3>
        <p>Este dicionário foi desenvolvido para a aula de PLNEB 2024/2025</p>
    """

    html_conceitos = "\n".join(f"""
        <div>
            <p><b>{designacao}</b></p>
            <p>{descricao}</p>
        </div>
        <hr/>
    """ for designacao, descricao in conceitos)

    html_footer = """
    </body>
    </html>
    """

    return html_header + html_conceitos + html_footer


html = gera_html(conceitos)

with open("dicionario_medico2.html", "w", encoding="UTF-8") as f_out:
    f_out.write(html)


