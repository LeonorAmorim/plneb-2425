from flask import Flask, request, render_template
import json
import re
app=Flask(__name__)

file=open("c:/Users/HP/Desktop/4Ano2Semestre/ProcLingNat/TPC5/LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="UTF-8")
texto=file.read()
file.close()


db_file=open("c:/Users/HP/Desktop/4Ano2Semestre/ProcLingNat/TPC5/_conceitos_.json",encoding="UTF-8") 
db=json.load(db_file)


@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route('/conceitos')
def conceitos():
    designacoes=list(db.keys())
    return render_template("conceitos2.html", designacoes=designacoes, title="Lista de conceitos")


@app.route('/api/conceitos')
def api_conceitos():
    return db

@app.route('/api/conceitos/<designacao>')
def api_conceito(designacao):

    return {"designacao":designacao, "descricao":db[designacao]}

@app.post("/conceitos")
def adicionar_conceito():
    descricao=request.form.get("descricao")
    designacao=request.form.get("designacao")
    db[designacao]=descricao
    f_out=open("_conceitos_.json","w", encoding="utf-8")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()
    #form_data

    designacoes=sorted(list(db.keys()))
    return render_template("conceitos2.html", designacoes=designacoes, title="Lista de Conceitos")


@app.route('/conceitos/<designacao>')
def conceito(designacao):
    designacoes=list(db.keys())
    if designacao in designacoes:
        descricao=db[designacao]
        return render_template("conceito2.html", designacao=designacao, descricao=db[designacao])
    else:
        return render_template("conceito2.html", designacao="Erro", descricao="Descrição não encontrada") 


@app.post("/conceitos")
def adicionar_conceito_api():
    data=request.get_json() 
    db[data["designacao"]]=data["descricao"]
    f_out=open("_conceitos_.json","w", encoding="UTF-8")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return data


def find_conceito(db,query,word_bound, case_sensitive):
    res=[]
    flags=0
    if word_bound=="on":
        pattern=r"\b("+query+r")\b"
    else:
        pattern="("+query+r")"
    if case_sensitive!="on":
        flags=re.IGNORECASE
    
    for designacao, descricao in db.items():
        if re.search(pattern, designacao, flags) or re.search(pattern, descricao, flags):
            bold_designacao=re.sub(pattern, r"<strong>\1</strong>", designacao, flags)
            bold_descricao=re.sub(pattern, r"<strong>\1</strong>", descricao, flags)
            res.append((designacao, bold_designacao,bold_descricao))
    return res

@app.route("/pesquisa")
def pesquisa():
    query=request.args.get("query")
    word_bound=request.args.get("word_bound")
    case_sensitive=request.args.get("case_sensitive")
    if not query:
        return render_template("pesquisa.html", title="Pesquisa")
    res=find_conceito(db,query,word_bound, case_sensitive)
    return render_template("pesquisa.html", conceitos=res, query=query, word_bound=word_bound, case_sensitive=case_sensitive, title="Pesquisa")

@app.delete("/conceitos/<designacao>")
def delete_conceito(designacao):
    if designacao in db:
        f_out=open("_conceitos_.json","w", encoding="UTF-8")
        del db[designacao]
        json.dump(db, f_out, indent=4, ensure_ascii=False)
        f_out.close()
        return {"success": True,"message": "Conceito apagado com sucesso", "redirect_url": "/conceitos", "data":designacao}
    
    return {"success": False ,"message": "Conceito não existe", "data":designacao}

@app.get("/conceitos/tabela")
def conceitos_tabela():
    return render_template("tabela.html")


@app.route("/tabela")
def tabela():
    query = request.args.get("query", "")
    use_regex = request.args.get("regex", "off") == "on"  # Checkbox para regex
    case_sensitive = request.args.get("case_sensitive", "off") == "on"  # Checkbox para case-sensitive

    conceitos = find_conceito(db, query, use_regex, case_sensitive)
    
    return render_template("tabela.html", conceitos=conceitos, query=query, use_regex=use_regex, case_sensitive=case_sensitive)

app.run(host="localhost", port=4002, debug= True)

#TPC acabar a tabela, meter os conceitos na tabela. Usar bootstrap 5 e ativar o regex