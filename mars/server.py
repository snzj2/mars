from flask import Flask, url_for

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
    return n +  f'''<h1>ЖДИ НАС МАРС!!!</h1>
            <br><img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
            <br>вот она, жди нас!'''

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
