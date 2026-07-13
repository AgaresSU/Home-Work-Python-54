from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
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


def show_data(session):
    for author in session.query(Author):
        print(author)

    print("*" * 50)

    for book in session.query(Book):
        print(book)


def main():
    create_database()
    session = Session()
    add_data(session)
    show_data(session)
    session.close()


if __name__ == "__main__":
    main()
