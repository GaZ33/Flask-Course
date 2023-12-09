from market import db, app



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
    # Criando a relação entre as tabelas
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    #função para nomear os items quando fizer a query pelo python shell
    def __repr__(self):
        return f'item {self.name}'


# criando outro model para o acesso de usuário
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=7000)
    # Criando uma relação entre as tabelas (uma foreign key do SQL)
    item = db.relationship('Item', backref='owned_user', lazy=True)

# Necessário para a criação do BD com essa tabela item
app.app_context().push()


