from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.config["SECRET_KEY"] = "plumbus-secret-key"

menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Каталог", "url": "/catalog"},
    {"name": "Сервис", "url": "/service"},
    {"name": "Контакты", "url": "/contact"},
]

plumbuses = [
    {
        "name": "Обычный плюмбус",
        "info": "Обычный домашний вариант. Его проще всего проверить и почистить.",
    },
    {
        "name": "Офисный плюмбус",
        "info": "На работе используется чаще, поэтому его лучше иногда проверять.",
    },
    {
        "name": "Подарочный плюмбус",
        "info": "Обычно стоит красиво, но его тоже иногда надо обслуживать.",
    },
]

services = [
    "Осмотр дингльбоба.",
    "Проверка грумбы.",
    "Чистка липлубиса.",
    "Пропитка шлимом.",
    "Настройка плюмбуса после долгого хранения.",
]

advice = [
    "Если плюмбус стал выглядеть не так, его лучше отнести в сервис.",
    "Если пропал комфорт, надо проверить флибовый сок.",
    "Если устройство долго стояло без дела, нужна простая профилактика.",
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Главная", menu=menu, advice=advice)


@app.route("/catalog")
def catalog():
    return render_template("catalog.html", title="Каталог", menu=menu, plumbuses=plumbuses)


@app.route("/service")
def service():
    return render_template("service.html", title="Сервис", menu=menu, services=services)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form["username"]) > 2:
            flash("Заявка отправлена успешно", category="success")
        else:
            flash("Ошибка отправки", category="error")

    return render_template("contact.html", title="Контакты", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
