from market import db, app
# Impotando a instancia para fazer a criptografia
from market import bcrypt
# Importando um decorator para fazer a sessão do login
from market import LoginManager
# Imprtando a classe que já possuem métodos para o user permanecer logado na sessão
from flask_login import UserMixin



# Criando nosso model com uma classe especial que diz para a nossa aplicação que é uma tabela
class Item(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    # Criando várias instância de uma classe column
    # Estamos dizendo que é um tipo string e um limite máximo de 30 caracteres, not null e unique
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    # Estamos dizendo que é um tipo integer e not null
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    # Criando a relação entre as tabelas
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    #função para nomear os items quando fizer a query pelo python shell
    def __repr__(self):
        return f'item {self.name}'
    
    def buy(self, user):
        # Atribuindo a nossa foreign key para o id do usuário
        self.owner = user.id
        # Subtraindo o money
        user.budget -= self.price
        # Realizando as alterações
        db.session.commit()




# Usando o decorator que será responsável pela sessão cada vez que alterar a página
@LoginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# criando outro model para o acesso de usuário
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=7000)
    # Criando uma relação entre as tabelas (uma foreign key do SQL)
    item = db.relationship('Item', backref='owned_user', lazy=True)

    # Criando uma função adicionar virgulas quando o número for muito grande
    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f"{str(self.budget)[:-3]},{str(self.budget)[-3:]}$"
        else:
            return f"{self.budget}$"

    # Usando o decorator para cada instância retornar o password
    @property
    def password(self):
        return self.password
    #  Usando outro decorator para cripgrafar nossa senha
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    # Função para verificar a senha hash com a que o usuário colocou no login
    def check_password_correction(self, attempted_password):
        # Essa função verifica para nós e retorna true or false
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    
    def can_purchase(self, item_objt):
        return self.budget >= item_objt.price
        
    

# Necessário para a criação do BD com essa tabela item
app.app_context().push()


