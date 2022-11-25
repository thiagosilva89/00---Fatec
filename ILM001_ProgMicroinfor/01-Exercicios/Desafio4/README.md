# Desenvolvimento-Web-Desafios

Criar um site com 3 páginas para uma universidade fictícia “UNES”.

Páginas: Home, Quem Somos e Contato.
## Como executar o projeto
<h3>Para executar o projeto é necessário ter instalado em seu computador o Pyhton 3</h3>

> Python 3.10 - https://www.python.org/ <br>

<h3>E ter instalado também o banco de dados Mariadb</h3>

> MariaDB - https://mariadb.com/kb/fr/ <br>

<h3>Após instalado deverá clonar o repositório</h3>

> https://github.com/acorreac/desenvolvimento-web-desafio
<br>

<h3>Subir o script do arquivo db-scrip.sql no gerenciador de banco de dados de seu preferencia(Workbanch, Dbeaver e etc) para criar o banco de dados<h3>

<h3>Se seu sistema operacional for Windows</h3>
<br>

![Windows](https://img.shields.io/badge/Windows-017AD7?style=for-the-badge&logo=windows&logoColor=white)

<h3>Deverá abrir o CMD e com o comando cd navegar até a pasta onde o repositório foi clonado e executar o segunte comando para criar o ambiente virtual:</h3>

```python
	python -m venv env
```

```python
	env\Scripts\Activate.ps1
```

<h3>Em seguida deverá instalar o Flask e o mariadb com o comando a baixo:</h3>

```python
	pip install flask
```

```python
	pip install mariadb
```

<h3>Após instalado corretamente, executar a aplicação através do comando:</h3>

```python
	flask run
```
ou

```python
	flask --app app --debug run
```
<br> 

<h3>Se seu sistema operacional for Linux</h3>
<br> 

![Linux](https://img.shields.io/badge/Linux-E34F26?style=for-the-badge&logo=linux&logoColor=black)

<h3>Deverá abrir o terminal e com o comando cd navegar até a pasta onde o repositório foi clonado e executar o seguinte comando para criar o ambiente virtual:</h3>

```python
	python3 -m venv env
```

```python
	source env/bin/activate
```

<h3>Em seguida deverá instalar o Flask e o mariadb com o comando a baixo:</h3>

```python
	pip install flask
```

```python
	pip install mariadb
```

<h4>E assim com o comando cd navegar até a pasta src, na qual contém o arquivo app.py e executar o seguinte comando:</h4>

```python
	flask run
```
ou

```python
	flask --app app --debug run
```

<h4>No terminal será mostrado uma mensagem com um link igual a este 'http://127.0.0.1:5000', na qual deverá ser copiado e colado no navegador de sua preferência para visualização da aplicação.</h4>

<h4>FIM</h4>

## Tecnologias

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

