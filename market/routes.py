# importando o decorator app do package
from market import app, db
# Importando o render_template e algumas outras funções
from flask import render_template, redirect, url_for, flash, get_flashed_messages
# Importando nossos modulos
from market.models import Item, User
# Importando nosso forms
from market.forms import RegisterForm, LoginForm
# Importando a instancia para os campos do login
from market import LoginManager
# Importando função para realizar o login
from flask_login import login_user

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
                          password=form.password1.data)
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

# Criando mais um route para o login
@app.route('/login', methods=['GET', 'POST'])
def login_page():
  # Criando o form para o user colocar os inputs
  form = LoginForm()
  # Condição que verifica se há ou não esse nome no BD
  if form.validate_on_submit():
    # Procura o user no BD
    attempted_user = User.query.filter_by(username=form.username.data).first()
    # Se encontrar o usur no BD:
    if attempted_user and attempted_user.check_password_correction(
              attempted_password=form.password.data
    ):
      login_user(attempted_user)
      flash(f'Sucess! You are logged in as: {attempted_user.username}', category='success')
      redirect(url_for('market_page'))
    else:
      flash('Username and password are not match! Please try again', category='danger')
  return render_template('login.html', form=form)









