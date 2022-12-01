from flask import render_template, url_for, request
from app import app
from db import mysql

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/quem-somos")
def quem_somos():
    return render_template('quemsomos.html')

@app.route('/contatos', methods=['GET', 'POST'])
def contatos():
    if request.method == "POST":
      email = request.form['email']
      assunto = request.form['assunto']
      descricao = request.form['descricao']

      cur = mysql.connection.cursor()
      cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))

      mysql.connection.commit()

      cur.close()

      return 'sucesso'

    return render_template('contato.html')

# rota usuários para listar todos os usuários no banco de dados.
@app.route('/users')
def users():
  cur = mysql.connection.cursor()

  users = cur.execute("SELECT * FROM contatos")

  if users > 0:
    userDetails = cur.fetchall()

    return render_template("users.html", userDetails=userDetails)