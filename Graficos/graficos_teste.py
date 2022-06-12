from util import bd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/grafico_exercicio')
def barras_03():
   mysql = bd.SQL("root", "", "lykke")
   comando = "SELECT intervalo, proporcao FROM exercicio_lazer"

   cs = mysql.consultar(comando, ())
   grf = ""
   for [intervalo, proporcao] in cs:
      grf += f", ['{intervalo}', {proporcao}, '#9999FF']"
   cs.close()

   return render_template('grafico_exercicio.html', barras_03=grf)

app.run(debug=True)