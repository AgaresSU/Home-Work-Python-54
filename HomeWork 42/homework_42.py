class Film:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.year})"


class FilmModel:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def get_all_films(self):
        return self.films

    def get_film(self, index):
        if 0 <= index < len(self.films):
            return self.films[index]
        return None

    def delete_film(self, index):
        if 0 <= index < len(self.films):
            return self.films.pop(index)
        return None


class FilmView:
    def show_menu(self):
        print("=" * 60)
        print("Редактирование данных каталога фильмов".center(60))
        print("=" * 60)
        print("Действия с фильмами:")
        print("1 - добавление фильма")
        print("2 - каталог фильмов")
        print("3 - просмотр определенного фильма")
        print("4 - удаление фильма")
        print("q - выход из программы")

    def get_action(self):
        return input("Выберите вариант действия: ")

    def get_film_data(self):
        title = input("Название фильма: ")
        genre = input("Жанр: ")
        director = input("Режиссер: ")
        year = input("Год выпуска: ")
        duration = input("Длительность: ")
        studio = input("Студия: ")
        actors = input("Актеры: ")
        return title, genre, director, year, duration, studio, actors

    def get_film_index(self):
        try:
            return int(input("Введите номер фильма: ")) - 1
        except ValueError:
            return -1

    def show_films(self, films):
        if not films:
            print("Каталог фильмов пуст")
        else:
            for index, film in enumerate(films, 1):
                print(f"{index}. {film}")

    def show_film(self, film):
        if film:
            print("=" * 60)
            print(f"Название фильма: {film.title}")
            print(f"Жанр: {film.genre}")
            print(f"Режиссер: {film.director}")
            print(f"Год выпуска: {film.year}")
            print(f"Длительность: {film.duration}")
            print(f"Студия: {film.studio}")
            print(f"Актеры: {film.actors}")
        else:
            print("Фильм не найден")

    def show_message(self, message):
        print(message)


class FilmController:
    def __init__(self):
        self.model = FilmModel()
        self.view = FilmView()

    def add_film(self):
        film_data = self.view.get_film_data()
        film = Film(*film_data)
        self.model.add_film(film)
        self.view.show_message("Фильм добавлен")

    def show_films(self):
        films = self.model.get_all_films()
        self.view.show_films(films)

    def show_one_film(self):
        self.show_films()
        index = self.view.get_film_index()
        film = self.model.get_film(index)
        self.view.show_film(film)

    def delete_film(self):
        self.show_films()
        index = self.view.get_film_index()
        film = self.model.delete_film(index)

        if film:
            self.view.show_message(f"Фильм {film.title} удален")
        else:
            self.view.show_message("Фильм не найден")

    def run(self):
        while True:
            self.view.show_menu()
            action = self.view.get_action()

            if action == "1":
                self.add_film()
            elif action == "2":
                self.show_films()
            elif action == "3":
                self.show_one_film()
            elif action == "4":
                self.delete_film()
            elif action == "q":
                break
            else:
                self.view.show_message("Неверный ввод")


def main():
    app = FilmController()
    app.run()


if __name__ == "__main__":
    main()
