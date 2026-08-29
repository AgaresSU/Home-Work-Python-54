import sqlite3


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        try:
            self.__cur.execute("SELECT title, url FROM mainmenu ORDER BY id")
            result = self.__cur.fetchall()
            if result:
                return result
        except sqlite3.Error as error:
            print("Ошибка чтения меню из базы данных", error)
        return []

    def get_page(self, alias):
        try:
            self.__cur.execute(
                "SELECT title, text FROM pages WHERE alias = ? LIMIT 1",
                (alias,),
            )
            result = self.__cur.fetchone()
            if result:
                return result
        except sqlite3.Error as error:
            print("Ошибка чтения страницы из базы данных", error)
        return False

    def get_page_items(self, alias):
        try:
            self.__cur.execute(
                "SELECT title, text FROM page_items "
                "WHERE page_alias = ? ORDER BY position",
                (alias,),
            )
            return self.__cur.fetchall()
        except sqlite3.Error as error:
            print("Ошибка чтения содержимого страницы", error)
        return []
