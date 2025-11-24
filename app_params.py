import requests
# import json
# URL = 'https://beautiful-soup-4.readthedocs.io/en/latest/'

# https://jsonplaceholder.typicode.com/posts?userId=6
BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

user_id = int(input('Upisite id korisnika: '))

PARAMS = {"userId": user_id}
# Dio headersa za autentikaciju preko JWT
HEADERS = {"Authentication": "Bearer JWT_TOKEN"}

# Ako se korisnik autorizira preko forme onda se salje kroz data
# NAPOMENA -> Onda ide POST, a ne GET
DATA = {"username": "pero", "password": "peric1"}
response = requests.post(BASE_URL,
                         params=PARAMS,
                         headers=HEADERS,
                         data=DATA)

try:
    response = requests.get(BASE_URL,
                            params=PARAMS,
                            headers=HEADERS)
    response.raise_for_status()

    posts = response.json()
    for post in posts:
        print()
        print(post)
        print()


except Exception as ex:
    print(f'Dogodila se greska: {ex}')