from flask import Flask, jsonify
from models import get_usuarios
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return "Desplegando página desde render. Solo tenemos 252 MB de espacio en el proyecto y la misma cantidad de espacio en BD"


@app.route("/usuarios", methods=["GET"])
def usuarios():
    lista = get_usuarios()
    return jsonify(lista)


if __name__ == "__main__":
    app.run(debug=True)
