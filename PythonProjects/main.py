import requests

base_url = 'https://api.pokemonbattle.me:9104/'
token = "31dc48f1075fe5ef785e57b360141809"

pokemon_id = ''

response_create_pokemon = requests.post(f'{base_url}pokemons', headers={"trainer_token" : token}, json={
    "name": "generate",
    "photo": "generate"
})

pokemon_id = response_create_pokemon.json()['id']
print(response_create_pokemon.text)

response_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers={"trainer_token" : token}, json={
    "pokemon_id": pokemon_id
})

print(response_pokeball.text)

response_rename_pokemon = requests.put(f'{base_url}pokemons', headers={"trainer_token" : token}, json={
    "pokemon_id": pokemon_id,
    "name": "cheburashka",
    "photo": ("https://dolnikov.ru/pokemons/albums/001.png")
})

print(response_rename_pokemon.text)