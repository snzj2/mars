from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surnmename = StringField('Фамилия пользователя', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    age = StringField('Возраст', validators=[DataRequired()])
    position = StringField('Позиция', validators=[DataRequired()])
    speciality = StringField('Специалитет', validators=[DataRequired()])
    adress = StringField('Адрес', validators=[DataRequired()])
    submit = SubmitField('Войти')
