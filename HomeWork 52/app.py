from flask import Flask, render_template


app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "/"},
    {"name": "Каталог", "url": "/catalog"},
    {"name": "Производство", "url": "/making"},
    {"name": "Руководство", "url": "/manual"},
]

facts = [
    "Плюмбус - это универсальное домашнее устройство.",
    "Тип устройства: домашнее.",
    "Главный эффект: комфорт.",
    "Создатель неизвестен, но само устройство есть почти у каждого.",
]

plumbuses = [
    {
        "name": "Обычный плюмбус",
        "text": "Подходит для дома, кухни, комнаты и других обычных дел.",
        "price": "6 1/2 бряблов",
    },
    {
        "name": "Офисный плюмбус",
        "text": "Стоит на рабочем месте и делает жизнь немного легче.",
        "price": "8 бряблов",
    },
    {
        "name": "Подарочный плюмбус",
        "text": "Красивый вариант, если надо подарить что-то полезное.",
        "price": "10 бряблов",
    },
]

steps = [
    "Берётся дингльбоб и пропитывается шлимом.",
    "Дингльбоб нанизываеться на грумбу.",
    "Втираем влиб в дингльбоб и пропитываем флибовым соком.",
    "Затем шлами теребит и плюёт на него.",
    "Блампсы гладим против чамблов.",
    "Липлубис из грумбо сбриваем.",
    "Плюмбус готов.",
]

rules = [
    "Хранить плюмбус в чистом месте.",
    "Не разбирать без причины.",
    "Иногда протирать мягкой тканью.",
    "Не давать грумбо пересыхать.",
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Главная", menu=menu, facts=facts)


@app.route("/catalog")
def catalog():
    return render_template("catalog.html", title="Каталог", menu=menu, plumbuses=plumbuses)


@app.route("/making")
def making():
    return render_template("making.html", title="Производство", menu=menu, steps=steps)


@app.route("/manual")
def manual():
    return render_template("manual.html", title="Руководство", menu=menu, rules=rules)


if __name__ == "__main__":
    app.run(debug=True)
