from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start_screen():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''<body>
                <div>
                  <p>Человечество вырастает из детства.</p> 
                  <p>Человечеству мала одна планета.</p> 
                  <p>Мы сделаем обитаемыми безжизненные пока планеты. </p> 
                  <p>И начнем с Марса! </p> 
                  <p>Присоединяйся!</p> 
                </div>
              </body>'''


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                 <head>
                   <meta charset="utf-8">
                   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <title>Привет, Марс!</title>
                 </head>
                 <body>
                   <h1>Жди нас, Марс!</h1>
                   <img src="{url_for('static', filename='img/mars_image.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                   <p>Вот она какая, красная планета.</p>
                 </body>
               </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                 <head>
                   <meta charset="utf-8">
                   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                   <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                   <title>Привет, Марс!</title>
                 </head>
                 <body>
                   <h1 class='promo__title'>Жди нас, Марс!</h1>
                   <img src="{url_for('static', filename='img/mars_image.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                   <div class="alerts">
                     <div class="alert alert-secondary" role="alert">
                       <h3>Человечество вырастает из детства.</h3>
                     </div>
                     <div class="alert alert-success" role="alert">
                       <h3>Человечеству мала одна планета.</h3>
                     </div>
                     <div class="alert alert-secondary" role="alert">
                       <h3>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
                     </div>
                     <div class="alert alert-warning" role="alert">
                       <h3>И начнем с Марса!</h3>
                     </div>
                     <div class="alert alert-danger" role="alert">
                       <h3>Присоединяйся!</h3>
                     </div>
                   </div>
                 </body>
               </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
