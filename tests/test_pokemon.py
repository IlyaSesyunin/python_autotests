import requests
import pytest

def test_status_code():
    token = '31dc48f1075fe5ef785e57b360141809'
    response = requests.get('https://api.pokemonbattle.me:9104/trainers')

    assert response.status_code == 200

def test_part_of_body():
    response = requests.get('https://api.pokemonbattle.me:9104/trainers', 
                            params={'trainer_id' : 4906})
    assert response.json()['trainer_name'] == 'Lolita'