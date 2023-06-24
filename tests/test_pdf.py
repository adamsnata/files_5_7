import os.path
from pypdf import PdfReader
from conftest import pdf_file, RESOURCE_PATH
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_pdf():
    if os.path.exists(RESOURCE_PATH):
        if os.path.isfile(pdf_file):
            reader = PdfReader(pdf_file)
            number_of_pages = len(reader.pages)
            page = reader.pages[0]
            text = page.extract_text()
            assert number_of_pages == 412
            assert 'pytest Documentation' in text
        else:
            print("Файл не найден.")