import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '68ba6b9f10339ec50dbeb37f0f4f649d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 33367

def test_statuse_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

    def test_part_of_response():
        response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
        assert response_get.json()['name'] == 'thecreator'
