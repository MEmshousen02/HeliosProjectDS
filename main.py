import csv
import pandas as pd

data = pd.read_csv('SolorFlare2004_05.csv')


with open('SolorFlare200405.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)