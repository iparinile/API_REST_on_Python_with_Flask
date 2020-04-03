from flask import (
    Flask,
    render_template
)

# Создадим экземпляр приложения
app = Flask(__name__, template_folder="templates")


# Создадим маршрут URL в своём приложении для "/"
@app.route('/')
def home():
    """
    Эта функция просто отвечает на URL "localhost:5000/" в
    адресной строке браузера
    :return:        представленный шаблон 'home.html'
    """
    return render_template('home.html')


# Если мы работаем в автономном режиме, запустим приложение
if __name__ == '__main__':
    app.run(debug=True)
