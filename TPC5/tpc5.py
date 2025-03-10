#### TPC 

from flask import Flask, request, render_template
import json
app=Flask(__name__)

file=open("c:/Users/HP/Desktop/4Ano2Semestre/ProcLingNat/TPC5/LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding="UTF-8")
texto=file.read()
file.close()


db_file=open("c:/Users/HP/Desktop/4Ano2Semestre/ProcLingNat/TPC5/_conceitos_.json",encoding="UTF-8") 
db=json.load(db_file)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

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

#TPC
@app.route('/conceitos/<designacao>')
def conceito(designacao):
    designacoes=list(db.keys())
    for i in designacoes:
        if i == designacao:
            return render_template("conceito2.html", designacao=designacao, descricao=db[designacao])
##

@app.post("/conceitos")
def adicionar_conceito():
    data=request.get_json() 
    db[data["designacao"]]=data["descricao"]
    f_out=open("_conceitos_.json","w", encoding="UTF-8")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return data


app.run(host="localhost", port=4002, debug= True)
