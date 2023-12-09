# Importando para fazer o forms
from flask_wtf import FlaskForm
# Importando campos especiais como string, num, password, data e etc
from wtforms import StringField, PasswordField, SubmitField
# Importando funções para validação
from wtforms.validators import Length, EqualTo, Email, DataRequired


# Criando nosso campo de registro
class RegisterForm(FlaskForm):
    # Criando o campo do username e preparando para validar ele
    username = StringField(label="Username", validators=[Length(min=2, max=30), DataRequired])
    # Datarequired faz com que seja necessário preencher o campo
    email_address = StringField(label="Email Address", validators=[Email(), DataRequired])
    # Criando 2 campos para a senha para validar elas
    password1 = PasswordField(label="Password", validators=[Length(min=6), DataRequired])
    # EqualTo valida se as senhas dão match
    password2 = PasswordField(label="Confirm Password", validators=[EqualTo('password1'), DataRequired])
    # Botão de enviar
    submit = SubmitField(label="Create Account")
