import random
import requests
import time


BASE_PHOTO_URL = 'https://robohash.org/'

def get_random_photo():
    robo_hash_id = random.randint(1, 5000)
    PHOTO_URL = f'{BASE_PHOTO_URL}/{robo_hash_id}'
    try:
        response = requests.get(PHOTO_URL)
        # response = requests.get(URL)
        response.raise_for_status()

        # content je binary -> odnosno file i koristi se za dohvat slika ili drugih datoteka
        with open(f'./RoboHashs/RoboHash-{robo_hash_id}.png', 'wb') as photo:
            photo.write(response.content)
            return f'Datoteka "RoboHash - {robo_hash_id}.png" je uspjesno kreirana !'


    except Exception as ex:
        print(f'Dogodila se greska: {ex}')

for i in range(10):
    get_random_photo()
    time.sleep(2)