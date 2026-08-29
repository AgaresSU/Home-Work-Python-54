import os
import sqlite3

from flask import Flask, abort, flash, g, render_template, request

from FDataBase import FDataBase


DATABASE = "plumbus.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = "plumbus-secret-key"
app.config["DATABASE"] = os.path.join(app.root_path, DATABASE)


def connect_db():
    con = sqlite3.connect(app.config["DATABASE"])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", mode="r", encoding="utf-8") as file:
        db.cursor().executescript(file.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


def get_page_data(alias):
    dbase = FDataBase(get_db())
    page = dbase.get_page(alias)
    if not page:
        abort(404)
    return dbase, page


@app.route("/")
@app.route("/index")
def index():
    dbase, page = get_page_data("index")
    return render_template(
        "index.html",
        title=page["title"],
        menu=dbase.get_menu(),
        page=page,
        items=dbase.get_page_items("index"),
    )


@app.route("/catalog")
def catalog():
    dbase, page = get_page_data("catalog")
    return render_template(
        "catalog.html",
        title=page["title"],
        menu=dbase.get_menu(),
        page=page,
        items=dbase.get_page_items("catalog"),
    )


@app.route("/service")
def service():
    dbase, page = get_page_data("service")
    return render_template(
        "service.html",
        title=page["title"],
        menu=dbase.get_menu(),
        page=page,
        items=dbase.get_page_items("service"),
    )


@app.route("/contact", methods=["POST", "GET"])
def contact():
    dbase, page = get_page_data("contact")

    if request.method == "POST":
        if len(request.form["username"]) > 2:
            flash("Заявка отправлена успешно", category="success")
        else:
            flash("Ошибка отправки", category="error")

    return render_template(
        "contact.html",
        title=page["title"],
        menu=dbase.get_menu(),
        page=page,
    )


if not os.path.exists(app.config["DATABASE"]):
    create_db()


if __name__ == "__main__":
    app.run(debug=True)
