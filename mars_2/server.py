from flask import Flask, url_for, render_template, redirect, request, abort, make_response, jsonify
from random import choice
from forms import loginform
from forms import jobform
import json
from data import db_session, jobs_api
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import reqparse, abort, Api, Resource
import users_resource


app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(jobs_api.blueprint)

    app.run()

api.add_resource(users_resource.UsersListResource, '/api/v2/users')


api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.route('/job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = jobform.JobForm()
    db_session.global_init("db/mars_explorer.db")
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                          ((Jobs.user == current_user) | (current_user.id == 1)
                                           | (current_user.id == Jobs.team_leader))
                                          ).first()
        if job:
            form.teamlead_id.data = job.team_leader
            form.job.data = job.job
            form.word_size.data = job.work_size
            form.collaborators.data = job.collaborators
            form.is_finished.data = job.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         ((Jobs.user == current_user) | (current_user.id == 1)
                                          | (current_user.id == Jobs.team_leader))
                                         ).first()
        if job:
            job.team_leader = form.teamlead_id.data
            job.job = form.job.data
            job.work_size = form.word_size.data
            job.collaborators = form.collaborators.data
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('job.html',
                           title='Редактирование новости',
                           form=form
                           )

@app.route('/job_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def job_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).filter(Jobs.id == id,
                                      ((Jobs.user == current_user) | (current_user.id == 1)
    | (current_user.id == Jobs.team_leader))
                                      ).first()
    print(news)
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')
@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/member')
def member():
    with open('templates/crew.json', encoding='utf-8') as cat_file:
        data = json.load(cat_file)
    k = choice(data)

    return render_template('member.html', name=k["name"], photo=k["photo"], work=", ".join(sorted(k["work"])))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginform.LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/distribution')
def distribution():
    user_list = ['Руслан', 'Ридли скотт', 'Энди Уир', 'Кирилл']
    return render_template('distribution.html', user_list=user_list)


@app.route('/job', methods=['GET', 'POST'])
@login_required
def add_news():
    form = jobform.JobForm()
    db_session.global_init("db/mars_explorer.db")
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()

        job.team_leader = form.teamlead_id.data
        job.job = form.job.data
        job.work_size = form.word_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data

        current_user.jobs.append(job)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('job.html', title='Добавление работы',
                           form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    db_session.global_init("db/mars_explorer.db")
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surnmename.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.adress.data,
            name=form.name.data,
            email=form.email.data,
        )

        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/')
def base():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    job = db_sess.query(Jobs).all()

    return render_template('spisook.html', news=job)


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')
