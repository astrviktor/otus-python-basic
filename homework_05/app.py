"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask, request, render_template, Blueprint

bootstrap_app = Blueprint(
    "index_app",
    __name__,
    url_prefix="/"
)

app = Flask(__name__)
app.register_blueprint(bootstrap_app)


@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")


@app.get("/about/", endpoint="about")
def get_about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
