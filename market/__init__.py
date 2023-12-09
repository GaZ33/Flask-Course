# Importando a instância Flask da biblioteca flask
from flask import Flask, render_template
# Importando a classe SQLAlchemy da ferramenta flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy




# Criando uma instância do Flask
app = Flask(__name__)
# Configurando o banco de dados da nossa aplicação e apontando para onde ele está
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# Criando uma senha para o nosso forms
app.config['SECRET_KEY'] = "edc3f2f78cd420d856afa59f"
# Você pode dar qualquer nome para o seu DB
# Criando uma instância da SQLAlchemy, precisamos passar nossa aplicação como argumento "app"
db = SQLAlchemy(app=app)

from market.models import Item




# Importando nossas rotas para a inicialização
from market import routes

