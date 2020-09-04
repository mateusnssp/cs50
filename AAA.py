import csv

with open("dictionary.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["word"])
