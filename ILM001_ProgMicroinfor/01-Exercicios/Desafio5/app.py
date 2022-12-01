from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL


def create_app():
    from app import routes
    routes.init_app(app)

    return app

app = Flask(__name__)




# conexão com o banco de dados
app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'fatec'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)


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
      cur.execute("INSERT INTO contatos(email, nome, assunto) VALUES (%s, %s, %s)", (email, assunto, descricao))

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


# run the app.
if __name__ == 'main':
    app.run(host='0.0.0.0', port=5000)

