from flask import Flask
from flask import request

app = Flask("ROOT")

@app.route("/")
def hello():
    return "Hello World!"


# exemplo para responder essa url: http://localhost:8000/noticias/brasil?categoria=ciencia&quantidade=2
@app.route("/noticias/<pais>")
@app.route("/noticias/<pais>/<estado>")
def lista_de_noticias(pais, estado=None):
    cat = request.args.get("categoria")
    qtd = request.args.get("quantidade")
    #noticias = BD.query(pais=pais, categoria=cat).limit(qtd)
    if not estado:
        estado = 'nenhum'
    noticias = 'Comedores de churros ' + cat + qtd + ' estado: ' + estado
    #return render_template("lista_de_noticias.html", noticias=noticias), 200
    return noticias


if __name__ == "__main__":
    app.run(debug=True)