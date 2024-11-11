from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<a href='index'>Главная страница</a>"

@app.route('/register')
def register():
    return render_template('register.html', title='Регистрация')

def login ():
    return render_template('login.html', title='Авторизация')

@app.errorhandler(404)
def page404():
    return render_template('page404.html', title='Ошибка 404')

