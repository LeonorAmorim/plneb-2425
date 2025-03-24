from flask import Flask, request, render_template
import json
app=Flask(__name__)

file=open("c:/Users/HP/Desktop/4Ano2Semestre/ProcLingNat/TPC5/LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="UTF-8")
texto=file.read()
file.close()


db_file=open("c:/Users/HP/Desktop/4Ano2Semestre/ProcLingNat/TPC6/_conceitos_.json",encoding="UTF-8") 
db=json.load(db_file)

resultados_file=open("c:/Users/HP/Desktop/4Ano2Semestre/ProcLingNat/TPC6/resultados.json",encoding="UTF-8") 
resultados=json.load(resultados_file)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route('/pesquisar')
def pesquisar():
    designacoes=list(db.keys())
    return render_template("pesquisar.html", designacoes=designacoes, title="Pesquisa")


@app.post('/pesquisar')
def pesquisar_conceito():
    termo_pesquisa = request.form.get("designacao").strip().lower()
    designacoes = list(db.keys())

    
    resultados = {key: db[key] for key in designacoes if termo_pesquisa in key.lower()}

    if resultados:
        
        with open("c:/Users/HP/Desktop/4Ano2Semestre/ProcLingNat/TPC6/resultados.json", "w", encoding="utf-8") as f_out:
            json.dump(resultados, f_out, indent=4, ensure_ascii=False)

        return render_template("pesquisar.html", resultados=resultados, designacoes=designacoes, title="Pesquisa")
    else:
        return render_template("pesquisar.html", resultados="Erro", designacoes=designacoes, title="Pesquisa")



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


app.run(host="localhost", port=4002, debug= True)

## TPC: Fazer o pesquisar funcionar, rota e uma nova página com caixa de texto, input,
#  botão de pesquisar e depois ao pesquisar aparece a entrada correspondente, só dos conceitos que deiam match,
#  depois tem de dizer onde houve match e ser clicável.