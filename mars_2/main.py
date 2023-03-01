from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    job = Jobs()
    job.team_leader = 3
    job.job = 'Менеджер модулей 2 и 5'
    job.work_size = 8
    job.collaborators = '2, 5'
    job.is_finished = False
    db_sess = db_session.create_session()

    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()