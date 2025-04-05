import os
from dotenv import load_dotenv
import requests
import json
import pokeData

POKEMONTCG_IO_URL = "https://api.pokemontcg.io/v2/cards"

load_dotenv()
# RestClient.configure(os.getenv("POKEMONTCG_IO_API_KEY"))
#
# try:
#     card = Card.where(q='name:charizard vmax*')
#     print(card)
# except HTTPError as e:
#     print(e)
#

def loadPokemonData():
    try:
        headers = {
            "X-Api-Key": os.getenv("POKEMONTCG_IO_API_KEY")
        }
        # params = {
        #     "select": "name,set,number,regulationMark,images,rarity"
        # }
        response = requests.get(POKEMONTCG_IO_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        with open("sample.json", "w") as output:
            json.dump(data, output)
        print('loaded all the pokemon data')

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code}, {e.response.text}")  # Print status code and response
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
    except KeyError as e:
        print(f"API response error: {e}, likely due to invalid API key or incorrect API format.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# try:
#     headers = {
#         "X-Api-Key": os.getenv("POKEMONTCG_IO_API_KEY")
#     }
#     params = {
#         "q": f'name:"eevee*"'
#     }
#     response = requests.get(POKEMONTCG_IO_URL, headers=headers, params=params)
#     response.raise_for_status()
#     data = response.json()

loadPokemonData()
with open('sample.json') as f:
    dataPoke = json.load(f)
if dataPoke:
    card = pokeData.find_first_regulation_mark_f_or_higher(dataPoke['data'])
    if card is None:
        print('No legal card by that name')
    else:
        card_name_response: str = card['name']
        card_image = card['images']['large']
        print(card)
else:
    print('couldnt find that pokemon')