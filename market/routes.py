# importando o decorator app do package
from market import app, db
# Importando o render_template e algumas outras funções
from flask import render_template, redirect, url_for, flash, get_flashed_messages
# Importando nossos modulos
from market.models import Item, User
# Importando nosso forms
from market.forms import RegisterForm

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
  # Fazendo a query para todos os items aparecerem no market
  items = Item.query.all()
  return render_template('market.html', items = items)

# Criando outro route para se registrar
@app.route("/register", methods=['GET', 'POST'])
def register_page():
  # Criando a instância do forms
  form = RegisterForm()
  # Validando os inputs do user
  if form.validate_on_submit():
    # Criando uma instância com os dados que o user colocou
    user_to_create = User(username=form.username.data,
                          email_address=form.email_address.data,
                          password_hash=form.password1.data)
    # Colocando para adicionar os dados 
    db.session.add(user_to_create)
    # Salvando os dados no DB
    db.session.commit()
    return redirect(url_for("market_page"))
  # Verificando se há um erro na validação, os erros vem em forma de dicionário
  if form.errors != {}:
    # Para cada error que o usuário fizer mostrará para ele com a função flash
    for err_msg in form.errors.values():
      flash(F"There was an error with creating a user: {err_msg}", category="danger")
  return render_template("register.html", form = form)

