import xlrd
import os.path
from conftest import xls_file, RESOURCE_PATH
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_xls():
    if os.path.exists(RESOURCE_PATH):
        if os.path.isfile(xls_file):
            book = xlrd.open_workbook(xls_file)
            print(f'Количество листов {book.nsheets}')
            print(f'Имена листов {book.sheet_names()}')
            sheet = book.sheet_by_index(0)
            print(f'Количество столбцов {sheet.ncols}')
            print(f'Количество строк {sheet.nrows}')
            print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=0, colx=1)}')
            # печать всех строк по очереди
            for rx in range(sheet.nrows):
                print(sheet.row(rx))

            assert sheet.ncols == 8
            assert sheet.nrows == 10
            assert book.sheet_names()[0] == 'Sheet1'
            assert sheet.cell_value(rowx=0, colx=1) == 'First Name'

        else:
            print("Файл не найден.")