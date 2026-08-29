CREATE TABLE IF NOT EXISTS mainmenu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS pages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alias TEXT NOT NULL,
    title TEXT NOT NULL,
    text TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS page_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page_alias TEXT NOT NULL,
    title TEXT NOT NULL,
    text TEXT,
    position INTEGER NOT NULL
);

DELETE FROM mainmenu;
DELETE FROM pages;
DELETE FROM page_items;

INSERT INTO mainmenu(title, url) VALUES
    ('Главная', '/'),
    ('Каталог', '/catalog'),
    ('Сервис', '/service'),
    ('Контакты', '/contact');

INSERT INTO pages(alias, title, text) VALUES
    ('index', 'Главная', '<p>Это продолжение сайта про плюмбусы. Здесь уже не столько про сам предмет, сколько про то, что с ним делать после покупки.</p>'),
    ('catalog', 'Каталог', '<p>В сервис можно принести разные плюмбусы. Главное, чтобы у них ещё была грумба и дингльбоб.</p>'),
    ('service', 'Сервис', '<p>Обслуживание нужно, чтобы плюмбус дольше работал нормально и не терял свой странный, но полезный эффект.</p>'),
    ('contact', 'Контакты', '<p>Здесь можно оставить заявку, если с плюмбусом что-то не так.</p>');

INSERT INTO page_items(page_alias, title, text, position) VALUES
    ('index', 'Совет 1', 'Если плюмбус стал выглядеть не так, его лучше отнести в сервис.', 1),
    ('index', 'Совет 2', 'Если пропал комфорт, надо проверить флибовый сок.', 2),
    ('index', 'Совет 3', 'Если устройство долго стояло без дела, нужна простая профилактика.', 3),
    ('catalog', 'Обычный плюмбус', 'Обычный домашний вариант. Его проще всего проверить и почистить.', 1),
    ('catalog', 'Офисный плюмбус', 'На работе используется чаще, поэтому его лучше иногда проверять.', 2),
    ('catalog', 'Подарочный плюмбус', 'Обычно стоит красиво, но его тоже иногда надо обслуживать.', 3),
    ('service', 'Осмотр дингльбоба', '', 1),
    ('service', 'Проверка грумбы', '', 2),
    ('service', 'Чистка липлубиса', '', 3),
    ('service', 'Пропитка шлимом', '', 4),
    ('service', 'Настройка после долгого хранения', '', 5);
