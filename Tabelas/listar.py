from util import bd
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


## Parque
@app.route('/listImgsParque')
def list_imgs():
    UPLOAD_FOLDER = '...\\static\\imagem_parque'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


    mysql = bd.SQL("root", "", "lykke")
    comando = "SELECT idt_parque, nome_parque, bairro, endereco, telefone, hr_funcionamento_parque, avaliacao_parque, foto_parque FROM parque;"
    imagens = ""
    cs = mysql.consultar(comando, [])
    for (idt, nome, bairro, end, tel, hrfunc, avaliacao, foto) in cs:
        imagens += "<TR>\n"
        imagens += "<TD>" + nome + "</TD>\n"
        imagens += "<TD>" + bairro + "</TD>\n"
        imagens += "<TD>" + end + "</TD>\n"
        imagens += "<TD>" + str(tel) + "</TD>\n"
        imagens += "<TD>" + hrfunc + "</TD>\n"
        imagens += "<TD>" + str(avaliacao) + "</TD>\n"
        imagens += "<TD><IMG SRC='" + foto + "'></TD>\n"
        imagens += "</TR>\n"

    return render_template('list_imgs_parque.html', imagens=imagens)

@app.route('/listImgsRestaurante')
def list_imgs_02():
    UPLOAD_FOLDER = '...\\static\\imagem_restaurante'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    mysql = bd.SQL("root", "", "lykke")
    comando = "SELECT idt_restaurante, nome_rest, bairro, endereco, telefone, hr_funcionamento_rest, avaliacao_rest, foto_rest FROM restaurante;"
    imagens = ""
    cs = mysql.consultar(comando, [])
    for (idt, nome, bairro, end, tel, hrfunc, avaliacao, foto) in cs:
        imagens += "<TR>\n"
        imagens += "<TD>" + nome + "</TD>\n"
        imagens += "<TD>" + bairro + "</TD>\n"
        imagens += "<TD>" + end + "</TD>\n"
        imagens += "<TD>" + str(tel) + "</TD>\n"
        imagens += "<TD>" + hrfunc + "</TD>\n"
        imagens += "<TD>" + str(avaliacao) + "</TD>\n"
        imagens += "<TD><IMG SRC='" + foto + "'></TD>\n"
        imagens += "</TR>\n"

    return render_template('list_imgs_restaurante.html', imagens=imagens)




app.run(debug=True)
