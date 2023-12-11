# Importando para fazer o forms
from flask_wtf import FlaskForm
# Importando campos especiais como string, num, password, data e etc
from wtforms import StringField, PasswordField, SubmitField
# Importando funções para validação
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
# Importando a instancia User
from market.models import User


# Criando nosso campo de registro
class RegisterForm(FlaskForm):
    # Função para verificar se já existe o username no BD
    def validate_username(self, username_to_check):
        # Fazendo a query para ver se existe, caso exista user receberá algum valor
        user = User.query.filter_by(username=username_to_check.data).first()
        # Se existir algum user irá entrar nessa condição
        if user:
            raise ValidationError('Username already exists! Please try a different username')
        
    # Fazendo a mesma coisa para o email
    def validate_email_address(self, email_address_to_check):
        email = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email:
            raise ValidationError('Email already exists! Please try a different Email')

    # Criando o campo do username e preparando para validar ele
    username = StringField(label="Username", validators=[Length(min=2, max=30), DataRequired()])
    # Datarequired faz com que seja necessário preencher o campo
    email_address = StringField(label="Email Address", validators=[Email(), DataRequired()])
    # Criando 2 campos para a senha para validar elas
    password1 = PasswordField(label="Password", validators=[Length(min=6), DataRequired()])
    # EqualTo valida se as senhas dão match
    password2 = PasswordField(label="Confirm Password", validators=[EqualTo('password1'), DataRequired()])
    # Botão de enviar
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label="Sign in")
