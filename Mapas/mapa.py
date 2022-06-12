from util import bd
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/icones")
def icones():
   sql = bd.SQL('root', '', 'lykke')
   cmd = 'SELECT idt_parque, latitude, longitude, nome_parque FROM parque'
   ## cmd = 'SELECT idt_restaurante, latitude, longitude, nome_rest FROM restaurante'
   ## cmd = 'SELECT idt_acad, latitude, longitude, nome_acad FROM academia'
   ## cmd = 'SELECT idt_cultural, latitude, longitude, nome_cult FROM cultural'
   cs = sql.consultar(cmd, [])
   marcadores = ''
   popups = ''
   icone = '{icon: lykkeicon}'
   for idt, lat, lng, nome in cs:
       marcadores += 'var mk_{} = L.marker([{}, {}], {}).addTo(m);\n'.format(idt, lat, lng, icone)
       popups += 'mk_{}.bindPopup("{}");'.format(idt, nome)
   cs.close()

   return render_template("icones.html", marcadores = marcadores, popups = popups)



app.run(debug=True)
