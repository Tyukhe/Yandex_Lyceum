from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired()])
    hashed_password = PasswordField('Пароль', validators=[DataRequired()])
    test_password = PasswordField('Повторить пароль', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    position = StringField('Профессия', validators=[DataRequired()])
    speciality = StringField('Спеацилизация', validators=[DataRequired()])
    address = StringField('Адресс', validators=[DataRequired()])
    submit = SubmitField('Регистрация')
