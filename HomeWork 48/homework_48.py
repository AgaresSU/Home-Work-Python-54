import sqlite3 as sq


products = [
    ("Хлеб", "продукты", 45, 30),
    ("Молоко", "продукты", 80, 20),
    ("Сыр", "продукты", 320, 12),
    ("Чай", "напитки", 150, 18),
    ("Кофе", "напитки", 410, 9),
    ("Сок", "напитки", 120, 16),
    ("Тетрадь", "канцелярия", 35, 40),
    ("Ручка", "канцелярия", 25, 55),
    ("Карандаш", "канцелярия", 18, 60),
    ("Мыло", "бытовая химия", 65, 25),
    ("Шампунь", "бытовая химия", 210, 14),
    ("Порошок", "бытовая химия", 480, 8),
    ("Яблоки", "фрукты", 130, 22),
    ("Груши", "фрукты", 160, 17),
    ("Бананы", "фрукты", 140, 19),
]


with sq.connect("homework_48.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS products")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        price INTEGER,
        count INTEGER
    )
    """)

    cur.executemany("""
    INSERT INTO products
    VALUES(NULL, ?, ?, ?, ?)
    """, products)

    cur.execute("SELECT * FROM products")

    for product in cur:
        print(product)
