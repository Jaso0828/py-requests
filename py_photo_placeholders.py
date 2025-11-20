import requests
import time


BASE_PHOTO_URL = 'https://placehold.co'

def get_random_photo(w: int, h: int = 400) -> str:
    PHOTO_URL = f'{BASE_PHOTO_URL}/{w}x{h}/png'
    try:
        response = requests.get(PHOTO_URL)
        # response = requests.get(URL)
        response.raise_for_status()

        # content je binary -> odnosno file i koristi se za dohvat slika ili drugih datoteka
        with open(f'./photos/placeholders/{w}x{h}.png', 'wb') as photo:
            photo.write(response.content)
            return f'Datoteka "{w}x{h}.png" je uspjesno kreirana!'

    except Exception as ex:
        print(f'Dogodila se greska: {ex}')


start_width = 400
for i in range(10):
    get_random_photo(start_width)
    start_width += 50
    time.sleep(2)