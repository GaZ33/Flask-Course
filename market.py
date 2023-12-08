# Importando a instância Flask da biblioteca flask
from flask import Flask, render_template
# Importando a classe SQLAlchemy da ferramenta flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Criando uma instância do Flask
app = Flask(__name__)

# Configurando o banco de dados da nossa aplicação e apontando para onde ele está
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# Você pode dar qualquer nome para o seu DB

# Criando uma instância da SQLAlchemy, precisamos passar nossa aplicação como argumento "app"
db = SQLAlchemy(app)

# Criando nosso model com uma classe especial que diz para a nossa aplicação que é uma tabela
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    # Criando várias instância de uma classe column
    # Estamos dizendo que é um tipo string e um limite máximo de 30 caracteres, not null e unique
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    # Estamos dizendo que é um tipo integer e not null
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'

app.app_context().push()



# Usando o decorator para que quando alguém entrar no root da página (home) execute a seguinte função 
@app.route("/")
# Usando outra route para acessar a mesma página. Você consegue acessar "home.html" pelos dois caminhos
@app.route("/home")
# Função que retorna a página html
def home_page():
  return render_template('home.html')

# Usando o decorator para quando alguém acessar o market exibir a página
@app.route("/market")
# Função que retorna o market.html
def market_page():
  items = Item.query.all()
  return render_template('market.html', items = items)



# É necessário utilizar essa abordagem para que a aplicação funcione corretamente
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)