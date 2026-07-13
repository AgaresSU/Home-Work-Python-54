from jinja2 import Environment, FileSystemLoader


menu = [
    {"url": "/index", "title": "Главная"},
    {"url": "/news", "title": "Новости"},
    {"url": "/about", "title": "О компании"},
    {"url": "/shop", "title": "Магазин"},
    {"url": "/contacts", "title": "Контакты"},
]

products = [
    {"name": "Ноутбук", "price": 65000},
    {"name": "Клавиатура", "price": 3500},
    {"name": "Мышь", "price": 1800},
]

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

tm = env.get_template("main.html")
msg = tm.render(
    title="Домашнее задание",
    header="Страница с домашним заданием",
    menu=menu,
    active="/index",
    products=products,
    footer_text="Домашнее задание выполнено",
)

print(msg)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(msg)
