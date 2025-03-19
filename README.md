# Discord Pokemon Card Bot

This is a Discord bot that allows users to search for Pokemon cards by name and display their images and details in the chat.

## Features

* **Card Search:** Users can search for Pokemon cards by name using the `!card <card name>` command.
* **Card Display:** The bot displays the card's image, name, set, card number, and rarity in an embedded message.
* **Error Handling:** The bot handles API errors, invalid card names, and other potential issues gracefully.
* **Partial Matching:** Allows users to search for cards using partial names.
* **Uses PokemonTCG.io API:** Retrieves card data from the PokemonTCG.io API.

## Prerequisites

* Python 3.6+
* Discord bot token
* PokemonTCG.io API key

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd ProfOak
    ```

2.  **Install dependencies:**

    ```bash
    pip install discord requests python-dotenv
    ```

3.  **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add your Discord bot token and TCGPlayer API key:

    ```
    DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
    POKEMONTCG_IO_API_KEY=YOUR_POKEMONTCG_IO_API_KEY
    ```

4.  **Enable Message Content Intent:**

    * In the Discord Developer Portal, go to your bot's page.
    * Navigate to the "Bot" tab.
    * Scroll down to "Privileged Gateway Intents" and enable "Message Content Intent."

5.  **Add your bot to your server:**

    * In the Discord Developer Portal, go to the "OAuth2" tab, then "URL Generator."
    * Select "bot" and "applications.commands" scopes.
    * Copy the generated URL and paste it into your browser to add the bot to your server.

## Usage

1.  **Run the bot:**

    ```bash
    python main.py
    ```

2.  **In your Discord server, use the `!card` command:**

    ```
    !card Pikachu
    !card Charizard VMAX
    ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## Author

Kevin Baltazar Reyes

## Acknowledgments

* [PokemonTCG.io](https://pokemontcg.io/)
* [Discord.py](https://discordpy.readthedocs.io/en/stable/)