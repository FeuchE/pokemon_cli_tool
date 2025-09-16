import argparse
import requests
import random
from rich.console import Console
from rich.table import Table

console = Console()
POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_total_pokemon():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1")
    if response.status_code == 200:
        return response.json()["count"]
    else:
        return 1010  # fallback

def get_pokemon_data(name_or_id):
    """Fetch Pokémon data from the PokéAPI."""
    url = f"{POKEAPI_BASE_URL}{name_or_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        console.print(f"[bold red]Error:[/bold red] Pokémon '{name_or_id}' not found.")
        return None
    else:
        console.print(f"[bold red]Error:[/bold red] Could not fetch data. (Status code: {response.status_code})")
        return None

def display_pokemon_info(data):
    """Display Pokémon info in a clean format using Rich tables."""

    # Define emoji mapping for Pokémon types
    type_emojis = {
        "normal": "😺",
        "fire": "🔥",
        "water": "💧",
        "electric": "⚡",
        "grass": "🌱",
        "ice": "❄️",
        "fighting": "🥊",
        "poison": "☠️",
        "ground": "🌍",
        "flying": "🕊️",
        "psychic": "🔮",
        "bug": "🐛",
        "rock": "🪨",
        "ghost": "👻",
        "dragon": "🐉",
        "dark": "🌑",
        "steel": "⚙️",
        "fairy": "🧚",
    }

    name = data["name"].capitalize()
    poke_id = data["id"]

    # Build type string with emojis
    type_list = []
    for t in data["types"]:
        type_name = t["type"]["name"]
        emoji = type_emojis.get(type_name, "❓")
        type_list.append(f"{emoji} {type_name.capitalize()}")

    types = ", ".join(type_list)
    
    sprite = data["sprites"]["front_default"]

    console.print(f"\n[bold yellow]{name}[/bold yellow] (#{poke_id})")
    console.print(f"[bold]Type(s):[/bold] {types}")
    console.print(f"[bold]Sprite:[/bold] {sprite}\n")

    # Display Base Stats
    table = Table(title="Base Stats")
    table.add_column("Stat", justify="left", style="cyan", no_wrap=True)
    table.add_column("Value", justify="center", style="magenta")

    for stat in data["stats"]:
        table.add_row(stat["stat"]["name"].capitalize(), str(stat["base_stat"]))

    console.print(table)

def main():
    parser = argparse.ArgumentParser(description="Pokémon Lookup CLI Tool")
    parser.add_argument("pokemon", nargs="?", help="Name of the Pokémon to look up (e.g., pikachu)")
    parser.add_argument("--random", action="store_true", help="Fetch a random Pokémon")
    args = parser.parse_args()

    if args.random:
        # Pick a random Pokémon by ID
        total = get_total_pokemon()
        random_id = random.randint(1, total)
        data = get_pokemon_data(random_id)
    elif args.pokemon:
        data = get_pokemon_data(args.pokemon)
    else:
        console.print("[bold red]Error:[/bold red] You must provide a Pokémon name or use --random.")
        return

    if data:
        display_pokemon_info(data)

if __name__ == "__main__":
    main()
