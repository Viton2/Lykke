from util import bd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/graficobarra')
def barras():
   mysql = bd.SQL("root", "", "bd_estatisticas_saude")
   comando = "SELECT intervalo, proporcao FROM autoavaliacao_saude"

   cs = mysql.consultar(comando, ())
   grf = ""
   for [intervalo, proporcao] in cs:
      grf += f", ['{intervalo}', {proporcao}, '#9999FF']"
   cs.close()

   return render_template('graficobarra.html', barras=grf)


@app.route('/doisgraficos')
def barras_02():
   mysql = bd.SQL("root", "", "bd_estatisticas_saude")
   comando = "SELECT intervalo, proporcao FROM consumo_hortalicas"

   cs = mysql.consultar(comando, ())
   grf = ""
   for [intervalo, proporcao] in cs:
      grf += f", ['{intervalo}', {proporcao}, '#F59443']"
   cs.close()

   comando_02 = "SELECT intervalo, proporcao FROM consumo_feijao"

   cs_02 = mysql.consultar(comando_02, ())
   grf_02 = ""
   for [intervalo, proporcao] in cs_02:
      grf_02 += f", ['{intervalo}', {proporcao}, '#00D4F7']"
   cs_02.close()

   return render_template('doisgraficos.html', barras_01=grf, barras_02=grf_02)

app.run(debug=1)
