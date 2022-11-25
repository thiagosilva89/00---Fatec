from flask import Flask, render_template, url_for, request
import db

app = Flask(__name__)

connection = db.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quem-somos')
def quem_somos():
    return render_template('quem-somos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        email = request.form['femail']
        assunto = request.form['fassunto']
        descricao = request.form['fdescricao']
        
        cur = connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES (?, ?, ?)", (email, assunto, descricao))
       
        connection.commit()
        
        cur.close()

        return 'Contato Enviado!'
    return render_template('contatos.html')

@app.route('/users')
def users():
    cur = connection.cursor()

    users = cur.execute("SELECT * FROM contato")

    if users != '':
        userDetails = cur.fetchall()

        return render_template("contatos.html", userDetails=userDetails)