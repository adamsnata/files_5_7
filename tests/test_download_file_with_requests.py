import os.path
import requests
from conftest import png_file, TMP_PATH

def test_downloaded_file_size():
    # TODO сохранять и читать из tmp, использовать универсальный путь
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    r = requests.get(url)

    if not os.path.exists(TMP_PATH):
        os.mkdir(TMP_PATH)
        with open(png_file, 'wb') as file:
            file.write(r.content)

        size = os.path.getsize(png_file)

        assert size == 30803
