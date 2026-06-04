import csv


data = [
    ["hostname", "vendor", "model", "location"],
    ["sw1", "Cisco", "3750", "London"],
    ["sw2", "Cisco", "3850", "Liverpool"],
    ["sw3", "Cisco", "3650", "Liverpool"],
    ["sw4", "Cisco", "3650", "London"]
]

with open("data.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";", lineterminator="\n")
    writer.writerows(data)

with open("data.csv", "r", encoding="utf-8") as f:
    file_reader = csv.reader(f, delimiter=";")
    for row in file_reader:
        print(row)
