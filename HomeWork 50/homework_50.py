from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, desc, distinct, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


DATABASE_NAME = "library.db"

engine = create_engine(f"sqlite:///{DATABASE_NAME}")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    country = Column(String(100))
    books = relationship("Book")

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __repr__(self):
        return f"Автор(ID: {self.id}, Имя: {self.name}, Страна: {self.country})"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    genre = Column(String(100))
    year = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))

    def __init__(self, title, genre, year, author_id):
        self.title = title
        self.genre = genre
        self.year = year
        self.author_id = author_id

    def __repr__(self):
        return f"Книга(ID: {self.id}, Название: {self.title}, Жанр: {self.genre}, Год: {self.year}, ID автора: {self.author_id})"


def create_database():
    Base.metadata.create_all(engine)


def add_data(session):
    if session.query(Author).count() > 0:
        return

    authors = [
        Author("Александр Пушкин", "Россия"),
        Author("Николай Гоголь", "Россия"),
        Author("Марк Твен", "США"),
        Author("Жюль Верн", "Франция"),
        Author("Артур Конан Дойл", "Великобритания"),
    ]

    for author in authors:
        session.add(author)

    session.commit()

    books = [
        Book("Капитанская дочка", "повесть", 1836, authors[0].id),
        Book("Евгений Онегин", "роман", 1833, authors[0].id),
        Book("Мертвые души", "поэма", 1842, authors[1].id),
        Book("Ревизор", "комедия", 1836, authors[1].id),
        Book("Том Сойер", "приключения", 1876, authors[2].id),
        Book("Гекльберри Финн", "приключения", 1884, authors[2].id),
        Book("Дети капитана Гранта", "приключения", 1868, authors[3].id),
        Book("Таинственный остров", "приключения", 1875, authors[3].id),
        Book("Собака Баскервилей", "детектив", 1902, authors[4].id),
        Book("Этюд в багровых тонах", "детектив", 1887, authors[4].id),
    ]

    for book in books:
        session.add(book)

    session.commit()


def print_query(title, data):
    print(f" {title} ".center(70, "="))
    for item in data:
        print(item)


def main():
    create_database()
    session = Session()
    add_data(session)

    print_query("1. Все авторы", session.query(Author).all())

    print_query("2. Все книги", session.query(Book).all())

    print_query("3. Книги после 1870 года", session.query(Book).filter(Book.year > 1870).all())

    print_query("4. Авторы из России", session.query(Author).filter(Author.country == "Россия").all())

    print_query("5. Приключенческие книги", session.query(Book).filter(Book.genre == "приключения").all())

    print_query(
        "6. Книги и авторы",
        session.query(Book.title, Author.name).join(Author).all()
    )

    print_query(
        "7. Количество книг у каждого автора",
        session.query(Author.name, func.count(Book.title)).join(Book).group_by(Author.name).all()
    )

    print_query(
        "8. Авторы, у которых больше одной книги",
        session.query(Author.name, func.count(Book.title)).join(Book).group_by(Author.name).having(func.count(Book.title) > 1).all()
    )

    print_query("9. Все жанры без повторов", session.query(distinct(Book.genre)).all())

    print_query("10. Пять самых новых книг", session.query(Book).order_by(desc(Book.year)).limit(5).all())

    session.close()


if __name__ == "__main__":
    main()
