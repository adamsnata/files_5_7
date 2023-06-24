import os.path
from pathlib import Path
from shutil import rmtree
import pytest
import shutil

PROJECT_ROOT_PATH = os.path.dirname(__file__)
RESOURCE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'resources'))
TMP_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'tmp'))

csv_name = 'users.csv'
zip_name = 'pytest-main.zip'
png_name = 'selenium_logo.png'
pdf_name = 'docs-pytest-org-en-latest.pdf'
xls_name = 'file_example_XLS_10.xls'
xlsx_name = 'file_example_XLSX_50.xlsx'
zip_archive_name = 'archive.zip'

csv_file = os.path.join(RESOURCE_PATH, csv_name)
zip_file = os.path.join(TMP_PATH, zip_name)
png_file = os.path.join(TMP_PATH, png_name)
pdf_file = os.path.join(RESOURCE_PATH, pdf_name)
xls_file = os.path.join(RESOURCE_PATH, xls_name)
xlsx_file = os.path.join(RESOURCE_PATH, xlsx_name)
zip_archive_file = os.path.join(RESOURCE_PATH, zip_archive_name)

@pytest.fixture(scope='session', autouse=True)
def remove_tmp_files():
    yield
    if os.path.exists(TMP_PATH):
        shutil.rmtree(TMP_PATH)