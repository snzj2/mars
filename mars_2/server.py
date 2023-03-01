from flask import Flask, url_for, render_template, redirect, request
from random import choice
from loginform import *
import json
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/training/<prof>')
def index(prof):
    return render_template('index.html', title='Заготовка', name=prof)


@app.route('/member')
def member():
    with open('templates/crew.json', encoding='utf-8') as cat_file:
        data = json.load(cat_file)
    k = choice(data)

    return render_template('member.html', name=k["name"], photo=k["photo"], work=", ".join(sorted(k["work"])))

@app.route('/login', methods=['GET', 'POST'])
def login():
    firstform = LoginForm()
    if firstform.validate_on_submit():
        print(request.form)
        print(request.form["username"])
        print(request.form["password"])
        print(request.form["username2"])
        print(request.form["password2"])
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=firstform)


@app.route('/distribution')
def distribution():
    user_list = ['Руслан', 'Ридли скотт', 'Энди Уир', 'Кирилл']
    return render_template('distribution.html', user_list=user_list)


@app.route('/')
def base():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return render_template('spisook.html', news=news)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    slovar = {
        "title": "asd",
        "surname": "Watny",
        "name": "Mark",
        "education": "Выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе",
        "ready": "True",
    }
    return render_template('answer.html', **slovar)


@app.route('/list_prof/<list>')
def spisok(list):
    k = ["инженер-исследователь", "пилот",
         "строитель", "экзобиолого", "врач",
         "инженер по терраформрованию",
         "климатолог", "специалист по радиационной защите",
         "астролог", " гляциолог",
         "инженер жизнеобеспечения",
         "метеоролог",
         "оператор марсохода",
         "киберинженер",
         "штурман",
         "пилот дронов"]
    return render_template('spisok.html', title='Заготовка', list=list, spisok=k)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')