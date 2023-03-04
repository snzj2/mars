from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job = StringField("Загаловок работы", validators=[DataRequired()])
    teamlead_id = StringField("ID тимлида", validators=[DataRequired()])

    word_size = StringField("Часы работ", validators=[DataRequired()])
    collaborators = StringField("Модули", validators=[DataRequired()])
    is_finished = BooleanField("закончен?")
    submit = SubmitField('Отправить работу')