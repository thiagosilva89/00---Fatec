#IMPORTANDO AS BIBLIOTECAS
from flask import Flask, render_template, url_for

#DEFININDO APP RUN COMO FLASK
app = Flask("__name__")


#DEFININDO DECORATOR PARA CHAMADA FUNÇÃO DE ROTA FLASK
@app.route('/')
#FUNÇÃO CHAMADA HOME 
def index():
    return render_template('index.html')


@app.route('/admin')
#FUNÇÃO CHAMADA HOME 
def admin():
    return render_template('admin.html')


#ROTA PARA SUBIDA DA APLICAÇÃO MAIN
if __name__ == "__main__":
    app.run(debug=True)