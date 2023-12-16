# importando o decorator app do package
from market import app, db
# Importando o render_template e algumas outras funções
from flask import render_template, redirect, url_for, flash, request
# Importando nossos modulos
from market.models import Item, User
# Importando nosso forms
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
# Importando a instancia para os campos do login
from market import LoginManager
# Importando função para realizar o login
from flask_login import login_user, logout_user, login_required, current_user

# Usando o decorator para que quando alguém entrar no root da página (home) execute a seguinte função 
@app.route("/")
# Usando outra route para acessar a mesma página. Você consegue acessar "home.html" pelos dois caminhos
@app.route("/home")
# Função que retorna a página html
def home_page():
  return render_template('home.html')

# Usando o decorator para quando alguém acessar o market exibir a página
@app.route("/market", methods=['GET', 'POST'])
# Usando o decorator para verificar se o usuário está logado antes de ir para a págida, e podemos pedir para que
# ele se registre
@login_required
# Função que retorna o market.html
def market_page():
  # Criando a instância do forms para comprar e vender
  purchase_form = PurchaseItemForm()
  # Quando o user clicar em comprar
  if request.method == "POST":
    # Consegue o nome do Item, como o nome é unico não teremos problema com duplacidade
    purchased_item =  request.form.get("purchased_item")
    # Procurando no DB se existe o item ou se alguém já comprou
    p_item_object = Item.query.filter_by(name=purchased_item).first()
    # Se existir ele não vai retornar como None e entrará nesse if
    if p_item_object:
      # Verificando se o user tem o money para comprar o item
      if current_user.can_purchase(p_item_object):
        p_item_object.buy(current_user)
        flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category="success")
      # Se ele não tiver money suficiente
      else:
        flash(f"Unfortunately! You do not have enough money to purchase {p_item_object.name}", category='danger')

    return redirect(url_for('market_page'))

  if request.method == "GET":
    # Fazendo a query para que os items que não tem owner aparecerem no market
    items = Item.query.filter_by(owner=None)
    return render_template('market.html', items = items, purchase_form = purchase_form)
  

  

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
    # Quando o usuário efutuar o register já sera logado com esse usuário que ele criou
    login_user(user_to_create)
      
    flash(f'Account created successfully! You are now logged in as: {user_to_create.username}', category='success')
    # Retornando para o market
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
      return redirect(url_for('market_page'))
    else:
      flash('Username and password are not match! Please try again', category='danger')
  return render_template('login.html', form=form)


# Criando a route para deslogar
@app.route('/logout')
def logout_page():
  # Função para deslogar
  logout_user()
  # Função para exibir que foi deslogado
  flash(F"You have been logged out", category="info")
  return redirect(url_for('home_page'))





