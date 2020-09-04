import csv

counts = {}

with open("dictionary.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["word"]
        if title in counts:
            counts[title] += 1
        else:
            counts[title] = 1

for title, count in counts.items():
    print(title, count, sep=" | ")