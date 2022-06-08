import mysql.connector
from flask import Flask, render_template


class SQL:
    def __init__(self, usuario, senha, esquema):
        self.cnx = mysql.connector.connect(user=usuario, password=senha,
                                           host='127.0.0.1',
                                           database=esquema)

    def executar(self, comando, parametros):
        cs = self.cnx.cursor()
        cs.execute(comando, parametros)
        self.cnx.commit()
        cs.close()
        return True

    def consultar(self, comando, parametros):
        cs = self.cnx.cursor()
        cs.execute(comando, parametros)
        return cs

    def __del__(self):
        self.cnx.close()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/alimentacao')
def alimentacao():
    return render_template('alimentacao.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/habitos')
def habitos():
    return render_template('habitos.html')


@app.route('/exercicio')
def exercicios():
    return render_template('exercicio.html')


@app.route('/lazer')
def lazer():
    return render_template('lazer.html')


@app.route('/saudeMental')
def saudeMental():
    return render_template('saudeMental.html')


app.run(debug=True)
