import csv
import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, url, file_name, pages):
        self.url = url
        self.file_name = file_name
        self.pages = pages
        self.res = []

    def get_html(self, url):
        response = requests.get(url)
        response.encoding = "utf-8"
        return response.text

    def parsing(self, html):
        soup = BeautifulSoup(html, "lxml")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            name = book.find("h3").find("a").get("title")
            price = book.find("p", class_="price_color").text.replace("\xa3", "GBP ")
            availability = book.find("p", class_="instock availability").text.strip()
            link = book.find("h3").find("a").get("href")

            self.res.append({
                "name": name,
                "price": price,
                "availability": availability,
                "url": link
            })

    def save(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\n")
            writer.writerow(["name", "price", "availability", "url"])

            for book in self.res:
                writer.writerow([
                    book["name"],
                    book["price"],
                    book["availability"],
                    book["url"]
                ])

    def run(self):
        for page in range(1, self.pages + 1):
            if page == 1:
                url = self.url
            else:
                url = f"{self.url}catalogue/page-{page}.html"

            html = self.get_html(url)
            self.parsing(html)
            print(f"Страница {page} обработана")

        self.save()
        print(f"Данные сохранены в файл {self.file_name}")


def main():
    parser = Parser("https://books.toscrape.com/", "books.csv", 5)
    parser.run()


if __name__ == "__main__":
    main()
