import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    data = []

    for book in books:
        name = book.find("h3").find("a").get("title")
        price = book.find("p", class_="price_color").text.replace("\xa3", "GBP ")
        availability = book.find("p", class_="instock availability").text.strip()
        url = "https://books.toscrape.com/" + book.find("h3").find("a").get("href")

        data.append({
            "name": name,
            "price": price,
            "availability": availability,
            "url": url
        })

    return data


def write_csv(data):
    with open("books.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        writer.writerow(["name", "price", "availability", "url"])

        for book in data:
            writer.writerow([
                book["name"],
                book["price"],
                book["availability"],
                book["url"]
            ])


def main():
    url = "https://books.toscrape.com/"
    data = get_data(get_html(url))
    write_csv(data)
    print("Данные сохранены в books.csv")


if __name__ == "__main__":
    main()
