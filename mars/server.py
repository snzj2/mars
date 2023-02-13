from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def apple():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/promotion')
def promotion():
    k = index()
    text = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!",
            "Юхууу!!!!!", "Присоединяйся!"]
    return k + "<br>".join(text)


@app.route('/image_mars')
def image_mars():
    n = promotion()
    return n + f'''<h1>ЖДИ НАС МАРС!!!</h1>
            <br><img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
            <br>вот она, жди нас!'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h2>Анкета претендента</h2>
                            <h3>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <label for="form-check"></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите email" name="email" >
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>дошкольное</option>
                                          <option>начальное</option>
                                          <option>основное</option>
                                          <option>среднее</option>
                                          <option>высшее</option>
                                        </select>
                                     </div>
                                    <label for="form-check">Какие у вас професии</label>
                                    <div class="form-check">
                                        <label for="form-check">Инженер-исследователь</label>
                                        <input class="form-check-input position-static" type="checkbox" id="blankCheckbox" value="option1" aria-label="...">
                                    </div>
                                    <div class="form-check">
                                        <label for="form-check">Инженер-строитель</label>
                                        <input class="form-check-input position-static" type="checkbox" id="blankCheckbox" value="option1" aria-label="...">
                                    </div>
                                    <div class="form-check">
                                        <label for="form-check">Пилот</label>
                                        <input class="form-check-input position-static" type="checkbox" id="blankCheckbox" value="option1" aria-label="...">
                                    </div>
                                    <div class="form-check">
                                        <label for="form-check">Метеролог</label>
                                        <input class="form-check-input position-static" type="checkbox" id="blankCheckbox" value="option1" aria-label="...">
                                    </div>
                                    <div class="form-check">
                                        <label for="form-check">Инженер по жизнеобеспечению</label>
                                        <input class="form-check-input position-static" type="checkbox" id="blankCheckbox" value="option1" aria-label="...">
                                    </div>
                                    <div class="form-check">
                                        <label for="form-check">Инженер по радиционной защите</label>
                                        <input class="form-check-input position-static" type="checkbox" id="blankCheckbox" value="option1" aria-label="...">
                                    </div>
                                    <div class="form-check">
                                        <label for="form-check">Врач</label>
                                        <input class="form-check-input position-static" type="checkbox" id="blankCheckbox" value="option1" aria-label="...">
                                    </div>
                                    <div class="form-check">
                                        <label for="form-check">Экзобиолог</label>
                                        <input class="form-check-input position-static" type="checkbox" id="blankCheckbox" value="option1" aria-label="...">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['accept'])

        return "Форма отправлена"


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result1(nickname, level, rating):
    n = promotion()
    return  f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                   <h2>Результаты отбора</h2>
                   <h3>Прентендент на участие в миссии {nickname}:</h3>
                    <div class="alert alert-dark" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-light" role="alert">
                      составляет {rating}
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>'''



@app.route('/promotion_image')
def promotion_image():
    n = promotion()
    return n + f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                   <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h1>ЖДИ НАС МАРС!!!</h1>
                    <br><img src="{url_for('static', filename='img/mars.jpg')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    
                    <div class="alert alert-dark" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-light" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


@app.route('/index')
def index():
    return "<h1>Миссия Колонизация Марса</h1><br><h2>И на Марсе будут яблони цвести!</h2>"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
