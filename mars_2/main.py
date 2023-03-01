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
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"

    user2 = User()
    user2.surname = "Том"
    user2.name = "Рэдл"
    user2.age = 86
    user2.position = "капитан 2"
    user2.speciality = "археолог"
    user2.address = "module_2"
    user2.email = "chief@mars.org"
    user2.hashed_password = "cap2"

    user3 = User()
    user3.surname = "Руслан"
    user3.name = "Баймухаметов"
    user3.age = 16
    user3.position = "я"
    user3.speciality = "археолог"
    user3.address = "module_3"
    user3.email = "Baimukhametuv@mars.org"
    user3.hashed_password = "necap"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()