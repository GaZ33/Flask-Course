# Importando a instância Flask da biblioteca flask
from flask import Flask

# Criando uma instância do Flask
app = Flask(__name__)

# Usando o decorator para que quando alguém entrar no root da página (home) execute a seguinte função 
@app.route("/")
# Função que retorna a página html
def hello_world():
  return "hello"

# Criando outro decorator para renderizar a página about
@app.route('/about')
def about_page():
     return 'a'



# É necessário utilizar essa abordagem para que a aplicação funcione corretamente
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)