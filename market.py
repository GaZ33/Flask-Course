# Importando a instância Flask da biblioteca flask
from flask import Flask, render_template

# Criando uma instância do Flask
app = Flask(__name__)

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
  items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
  return render_template('market.html', items = items)



# É necessário utilizar essa abordagem para que a aplicação funcione corretamente
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)