import requests
import json


URL = 'https://dummyjson.com/recipes'

try:
    response = requests.get(URL)
    response.raise_for_status()

    # content je binary -> odnosno file i koristi se za dohvat slika ili drugih datoteka
    # print(response.content)
    
    txt_data = response.text
    recipes_dict = json.loads(txt_data)
    print(recipes_dict)
    for recipe in recipes_dict['recipes']:
        print(recipe)
        print()

    # Kraci nacin za konverziju u dict
    recipes = response.json()
    for recipe in recipes['recipes']:
        print(recipe)
        print()



except Exception as ex:
    print(f'Dogodila se greska: {ex}')