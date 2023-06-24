import csv
import os.path
from conftest import csv_file
# TODO оформить в тест, добавить ассерты и использовать универсальный путь


rows = [['Anna', 'Pavel', 'Peter'],
       ['Alex', 'Serj', 'Yana']]


def test_csv():
    if not os.path.exists(csv_file):
        with open(csv_file, 'w') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            for row in rows:
                csvwriter.writerow(row)
    else:
        with open(csv_file) as csvfile:
            csvreader = csv.reader(csvfile)
            rows_from_csv = []
            for row in csvreader:
                rows_from_csv.append(row)

    assert rows == rows_from_csv
