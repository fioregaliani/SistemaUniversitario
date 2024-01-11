from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class RegisterForm(FlaskForm):
    username = StringField("Nombre Usuario", validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Contraseña', validators=[DataRequired(), Length(min=8), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField(label='Repetir Contraseña', validators=[DataRequired()])
    name = StringField("Nombre", validators=[DataRequired()])
    lastname = StringField("Apellido", validators=[DataRequired()])
    claustro = SelectField('Claustro', choices=[('Estudiante', 'Estudiante'),('Docente', 'Docente'),('PAyS', 'PAyS')])
    submit = SubmitField(label='Registrarse')
    
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Contraseña', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Ingresar')