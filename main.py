import discord
import requests
import os
from dotenv import load_dotenv
from typing import Final

load_dotenv()  # Load environment variables from .env file

TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
POKEMONTCG_IO_URL: Final[str] = "https://api.pokemontcg.io/v2/cards"

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

client = discord.Client(intents=intents)

def find_first_legal_standard(pokelist): #not working correctly because the Pokemon API is not up to date
  for pokemans in pokelist['data']:
    if 'legalities' in pokemans and 'standard' in pokemans['legalities'] and pokemans['legalities']['standard'] == 'Legal':
      return pokemans
  return None

def find_first_regulation_mark_f_or_higher(pokelist):
    """
    Finds and returns the first entry in the 'pokelist' list where
    'regulationMark' is 'F', 'G', 'H', or a letter that comes later in the alphabet.

    Args:
        pokelist: A dictionary containing a 'data' list of entries.

    Returns:
        The first entry where 'regulationMark' is 'F', 'G', 'H', or higher,
        or None if no such entry is found.
    """
    for pokeman in pokelist['data']:
        if 'regulationMark' in pokeman and pokeman['regulationMark'] >= 'F':
            return pokeman
    return None

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!card'):
        card_name = message.content[6:].strip()  # Extract card name after "!card "
        if not card_name:
            await message.channel.send("Please provide a card name. Example: `!card Pikachu`")
            return

        try:
            headers = {
                "X-Api-Key": os.getenv("POKEMONTCG_IO_API_KEY")
            }
            params = {
                "q": f'name:"{card_name}*"' # Using wildcard for partial matches
            }

            response = requests.get(POKEMONTCG_IO_URL, headers=headers, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            data = response.json()

            if data['data']:
                card = find_first_regulation_mark_f_or_higher(data) #Get first card of results
                if card is None:
                    await message.channel.send(f"'{card_name}' is not legal in standard.")
                else:
                    card_name_response = card['name']
                    card_image = card['images']['large']

                    embed = discord.Embed(title=card_name_response, color=0x00B0F0) # Embed for better formatting
                    embed.set_image(url=card_image)

                    if 'set' in card:
                        embed.add_field(name="Set", value=card['set']['name'], inline=True)
                    if 'number' in card:
                        embed.add_field(name="Card Number", value=card['number'], inline=True)
                    if 'rarity' in card:
                        embed.add_field(name="Rarity", value=card['rarity'], inline=True)

                    await message.channel.send(embed=embed)

            else:
                await message.channel.send(f"Could not find a card named '{card_name}'.")

        except requests.exceptions.HTTPError as e:
            await message.channel.send(f"HTTP error occurred: {e}")
            print(f"HTTP error: {e.response.status_code}, {e.response.text}")  # Print status code and response
        except requests.exceptions.RequestException as e:
            await message.channel.send(f"An error occurred: {e}")
            print(f"API request failed: {e}")
        except KeyError as e:
            await message.channel.send(f"An unexpected API response error occurred: {e}")
            print(f"API response error: {e}, likely due to invalid API key or incorrect API format.")
        except Exception as e:
            await message.channel.send(f"An unexpected error occurred: {e}")
            print(f"Unexpected error: {e}")

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()