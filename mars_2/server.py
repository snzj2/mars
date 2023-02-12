from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def index(prof):
    return render_template('index.html', title='Заготовка', name=prof)


@app.route('/')
def base():
    return render_template('base.html', title='Заготовка')


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
