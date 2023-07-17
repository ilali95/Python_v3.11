import csv
import random

def generate_csv(filename, rows):
    with open(filename, 'w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.random() for _ in range(3)]
            writer.writerow(row)
