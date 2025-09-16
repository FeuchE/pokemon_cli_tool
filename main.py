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

def get_evolution_chain(species_url):
    """Fetch and return evolution chain as a list of Pokémon names with error handling."""
    try:
        response = requests.get(species_url, timeout=5)
        response.raise_for_status()
        species_data = response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error:[/bold red] Failed to fetch species data: {e}")
        return []

    # Safely get the evolution chain URL
    evolution_chain_url = species_data.get("evolution_chain", {}).get("url")
    if not evolution_chain_url:
        console.print("[bold yellow]No evolution chain found for this Pokémon.[/bold yellow]")
        return []

    try:
        evo_response = requests.get(evolution_chain_url, timeout=5)
        evo_response.raise_for_status()
        evolution_data = evo_response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error:[/bold red] Failed to fetch evolution chain data: {e}")
        return []

    chain = evolution_data.get("chain")
    if not chain:
        console.print("[bold yellow]No evolution data found in the API response.[/bold yellow]")
        return []

    evolution_list = []

    # Recursive helper function to traverse chain
    def traverse(chain_link):
        evolution_list.append(chain_link["species"]["name"].capitalize())
        for evo in chain_link.get("evolves_to", []):
            traverse(evo)

    try:
        traverse(chain)
    except KeyError as e:
        console.print(f"[bold red]Error:[/bold red] Malformed evolution data: missing key {e}")
        return []

    return evolution_list

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

    # Fetch and display evolution chain
    try:
        evolution_list = get_evolution_chain(data["species"]["url"])
        if len(evolution_list) > 1:
            console.print(f"[bold cyan]Evolution Chain:[/bold cyan] {' → '.join(evolution_list)}\n")
    except Exception as e:
        console.print(f"[bold red]Warning:[/bold red] Could not fetch evolution chain. ({e})\n")

    # Display Base Stats
    table = Table(title="Base Stats")
    table.add_column("Stat", justify="left", style="cyan", no_wrap=True)
    table.add_column("Value", justify="center", style="magenta")

    for stat in data["stats"]:
        table.add_row(stat["stat"]["name"].capitalize(), str(stat["base_stat"]))

    console.print(table)

def list_pokemon_by_type(type_name):
    """Fetch and list the first 20 Pokémon of a given type."""
    url = f"https://pokeapi.co/api/v2/type/{type_name.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        console.print(f"[bold red]Error:[/bold red] Type '{type_name}' not found.")
        return

    data = response.json()
    pokemon_list = data["pokemon"][:20]  # select first 20 Pokémon

    console.print(f"\n[bold green]First 20 Pokémon of type '{type_name.capitalize()}':[/bold green]")
    for i, entry in enumerate(pokemon_list, start=1):
        name = entry["pokemon"]["name"].capitalize()
        console.print(f"{i}. {name}")

def get_random_pokemon():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=2000")
    if response.status_code == 200:
        results = response.json()["results"]
        random_pokemon = random.choice(results)
        return get_pokemon_data(random_pokemon["name"])
    else:
        console.print("[bold red]Error:[/bold red] Could not fetch Pokémon list.")
        return None

def main():
    parser = argparse.ArgumentParser(description="Pokémon Lookup CLI Tool")
    parser.add_argument("pokemon", nargs="?", help="Name of the Pokémon to look up (e.g., pikachu)")
    parser.add_argument("--random", action="store_true", help="Fetch a random Pokémon")
    parser.add_argument("--type", help="List the first 20 Pokémon of a given type (e.g., fire, water)")
    args = parser.parse_args()

    if args.type:
        list_pokemon_by_type(args.type)
        return
    elif args.random:
        data = get_random_pokemon()
    elif args.pokemon:
        data = get_pokemon_data(args.pokemon)
    else:
        console.print("[bold red]Error:[/bold red] You must provide a Pokémon name or use --random.")
        return

    if args.pokemon or args.random:
        if data:
            display_pokemon_info(data)

if __name__ == "__main__":
    main()
