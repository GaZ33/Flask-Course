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






# É necessário utilizar essa abordagem para que a aplicação funcione corretamente
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)