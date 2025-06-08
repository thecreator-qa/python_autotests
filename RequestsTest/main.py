import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '68ba6b9f10339ec50dbeb37f0f4f649d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "URL_LOGIN",
    "password": "URL_PASSWORD"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

body_change_name = {
    "pokemon_id": "333295",
    "name": "G63",
    "photo_id": 377
}

body_pokeball = {
    "pokemon_id": "333295"
}

response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)

response_confirmation = requests.post (url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)
              

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name).text

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)