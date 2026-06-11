import csv
import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, url, file_name, pages):
        self.url = url
        self.file_name = file_name
        self.pages = pages

    def get_html(self, page):
        if page == 1:
            url = self.url
        else:
            url = f"{self.url}catalogue/page-{page}.html"

        response = requests.get(url)
        response.encoding = "utf-8"
        return response.text

    def get_data(self, html):
        soup = BeautifulSoup(html, "html.parser")
        books = soup.find_all("article", class_="product_pod")
        data = []

        for book in books:
            name = book.find("h3").find("a").get("title")
            price = book.find("p", class_="price_color").text.replace("\xa3", "GBP ")
            availability = book.find("p", class_="instock availability").text.strip()
            link = book.find("h3").find("a").get("href")

            if not link.startswith("catalogue/"):
                link = "catalogue/" + link

            data.append({
                "name": name,
                "price": price,
                "availability": availability,
                "url": self.url + link
            })

        return data

    def write_csv(self, data):
        with open(self.file_name, "a", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\n")

            for book in data:
                writer.writerow([
                    book["name"],
                    book["price"],
                    book["availability"],
                    book["url"]
                ])

    def run(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\n")
            writer.writerow(["name", "price", "availability", "url"])

        for page in range(1, self.pages + 1):
            html = self.get_html(page)
            data = self.get_data(html)
            self.write_csv(data)

        print(f"Данные сохранены в файл {self.file_name}")


def main():
    parser = Parser("https://books.toscrape.com/", "books.csv", 3)
    parser.run()


if __name__ == "__main__":
    main()
