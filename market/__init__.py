# Importando a instância Flask da biblioteca flask
from flask import Flask
# Importando a classe SQLAlchemy da ferramenta flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# Importando a classe para criptografar as senhas
from flask_bcrypt import Bcrypt
# Importando a classe para cuidar do nosso login
from flask_login import LoginManager



# Criando uma instância do Flask
app = Flask(__name__)
# Configurando o banco de dados da nossa aplicação e apontando para onde ele está
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# Criando uma senha para o nosso forms
app.config['SECRET_KEY'] = "edc3f2f78cd420d856afa59f"
# Você pode dar qualquer nome para o seu DB
# Criando uma instância da SQLAlchemy, precisamos passar nossa aplicação como argumento "app"
db = SQLAlchemy(app=app)

# Criando a instância da criptografia para reconhecer a aplicação
bcrypt = Bcrypt(app)

# Criando a instância da classe que irá cuidar do login para reconhecer a aplicação
LoginManager = LoginManager(app)

# Fazendo com que reconheça onde é a nossa página de login para redirecionar o user
LoginManager.login_view = "login_page"

# Alterando a flash message que aparece quando vc é redirecionado para login page
LoginManager.login_message_category = "info"

# Importando nossas rotas para a inicialização
from market import routes

