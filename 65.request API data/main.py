# How to connect to an API using Python
import requests                                 # pip install requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokeman_info(name):               # remeber your parameter can be named different than your arguments
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrive data {response.status_code}")

# pokemon_name = "pikachu"
pokemon_name = "Typhlosion"
pokemon_info = get_pokeman_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

