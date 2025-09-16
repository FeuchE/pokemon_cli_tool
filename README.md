# PokéCLI: Project Documentation
Explore, discover, and get stats on any Pokémon instantly. 

## 🌍 Project overview
Introducing my **PokéCLI!** A Python-based command-line Pokédex clone that lets users look up Pokémon stats, types, and evolution chains, with support for random Pokémon discovery.  
‍
- 🎯 **The goal:** Create a Python API-powered mini app
- 🛠 **Tech-stack:** Python 3.13
- 🛠 **Tools:** PokéAPI, Requests, JSON, Argparse, and Rich
‍
- 📆 **Dates:** Dates: September 2025
- 📆 **Duration:** 2 days 

---

## 📣 The pitch

**The problem:**
Do you love Pokémon but can't remember the stats and evolution for every Pokémon?

**The solution:**
A new command-line app where you can quickly look-up a Pokémon's stats and evolutions.

**The target audience:**
- Demographic 1: 20-40 year olds who grew up with Pokémon and want to rediscover their love for it. 
- Demographic 2: 5-15 year olds who want to get into Pokémon and build up their knowledge.

**The features:**
- Lookup a Pokémon's types, ID, sprite and base stats.
- Fetch a random Pokémon.
- See the evolution chain for a Pokémon.
- Type filter that lists 20 Pokémon from a type inputted by the user.

---

## ✨💡🌟 What did I learn?
- **API Integration & JSON Handling:** I learned how to fetch data from REST APIs, parse nested JSON responses, and traverse data structures like evolution chains.
- **Error Handling & Defensive Coding:** I implemented robust error handling to prevent crashes from bad network responses, missing data, or user input errors.
- **Command-Line App Design:** I built a clean CLI interface with flags like --random and --type, practicing argparse to handle multiple user flows.
- **Code Modularity & Reuse:** I structured my code into small, testable functions (get_pokemon_data, get_evolution_chain, etc.), making the app easier to maintain and extend.
- **User Experience in a CLI Environment:** I used rich for tables, colors, and emojis, making the CLI visually appealing and fun to use; even without a GUI.
- **Version Control Workflow:** I created feature branches, pushed to GitHub, and practiced merging via Pull Requests, simulating a professional workflow.

---

## 🚧 Challenges

**1. Random Pokémon Lookup**
- **Challenge**: I wanted the CLI to be more engaging than just a name lookup. Firstly, I needed to know how many total Pokémon existed in the API. Hardcoding this number would be brittle, as the PokéAPI updates with new generations, my app would break or miss data. 
- **Solution**: I implemented a helper function get_total_pokemon() that queries the PokéAPI’s list endpoint with a limit=0 parameter to dynamically retrieve the total count. I then used Python’s random.randint() to select a random Pokémon ID within that range. Lastly, I passed the random ID into my existing get_pokemon_data() function for a seamless experience.
- **Outcome**: Users can now run py main.py --random to instantly discover a random Pokémon. The solution implements scalable and dynamic architecture to automatically keep up with new Pokémon generations without manual code updates.
  
**2. Emoji Type Display**
- **Challenge**: I initially displayed Pokémon types as plain text, which looked flat and uninteresting. I wanted to add some visual flair to make the CLI output feel polished and fun; despite being a text-only app. 
- **Solution**: I created a dictionary mapping each Pokémon type to a unique emoji through key:value pairs (e.g. {"fire": "🔥", "water": "💧", "grass": "🌱"}). When displaying types, I look them up in the dictionary and fallback to a default emoji if unknown.
- **Outcome**: Type information is now instantly recognizable and visually engaging. Adds personality and polish, making the CLI feel more like a true Pokédex experience.

**3. Type Filter**
- **Challenge**: Users could only look up one Pokémon at a time; there was no way to browse groups of Pokémon by type. I wanted to add a way to explore, for example, the first 20 Fire-type Pokémon. 
- **Solution**: I added a --type argument using argparse to accept a type name from the user. I implemented list_pokemon_by_type() to: fetch the type endpoint (e.g. /type/fire), extract all Pokémon in that type, and print the first 20 names in a clean numbered list.
- **Outcome**: Users can now quickly explore Pokémon by category. By creating a mini "browse mode," I added depth to my app beyond individual lookups. 

**4. API**
- **Challenge**: Pokémon evolutions aren’t included in the main Pokémon endpoint.
- **Solution**: I used two API calls (species + evolution chain). I fetched the species endpoint, then extracted the evolution chain URL. I then utilised recursive traversal of the nested evolution chain object. Lastly, I added error handling to catch edge cases or network failures.
- **Outcome**: Added a richer, more informative Pokédex experience. Also, demonstrated my ability to handle nested data structures. Robust error handling prevents crashes on missing data or API issues. 

---

## 🚧 Error handling

**1. General API related error handling**
- **Challenge**: To stop my app crashing when encountering edge cases or network failures. For example, if PokéAPI is overloaded, there are API errors, slow responses, or invalid URLs. 
- **Solution**: I added Try/Except error handling to catches network errors and timeouts. I tested blocks of code for errors in the try blocks. Then handled errors in the except blocks.

**2. Network Error Handling**
- **Challenge**: Connection errors, timeouts, and 404/500 responses.
- **Solution**: I used requests.exceptions.RequestException to catch connection errors and timeouts. I also used .raise_for_status() to catch 404/500 responses cleanly. Lastly, I prevented the CLI from hanging forever if the API is slow (timeout=5).  

**3. Handling edge cases**
- **Challenge**: Pokémon with no evolutions, missing data, and missing keys.  
- **Solution**: I used .get() with defaults instead of direct dictionary indexing to avoid KeyError. If there is no evolution data, the function now returns an empty list, so the calling function can skip displaying it, rather than crashing, and displays an informative error message to the user.

---

## 🏆 Accomplishments

**✅Technical Skills:**
- Handling data retrieval and formatting.
- Using requests for API calls.
- Using JSON parsing for API integration.
- Organise Pokémon stats to display in the command-line.
- Fully functional CLI with multiple commands/flags. 

**✅Design Skills:**
- Displayed stats in a table so its easy to read.
- Using Rich for colourful, tabular CLI output.
- I used dictionary mapping, for loop, arrays, and concatenation to create a list of a Pokémon's types with relevant emojis, to improve the user experience.

---

## 💡 Planning

**Creating action plan:**
I utilised AI to help me break down the project into manageable steps. I mapped out how to create the basic API-powered mini app. Then wrote a list of additional features I would like to add to improve the game play and user experience. I then prioritised the additional features as I had a 2 day deadline. I will continue working on the project in the future as I expand my Python knowledge, adding the other feaures.

---

## 📊 Project management

**Git version control:**
- To manage the progress of the project I used Git version control to push each stage of the project via a new branch using detailed descriptions.
- This has advantages for other developers as well as myself. It clearly explains the steps I took in order to add additional features. It also enabled me to revert to previous versions of my code, if I encountered an error whilst adding a new feature.
- I used Copilot to review my pull requests as this was a solo project.

**Kanban board:**
- To manage my project I created a KanBan board using Github projects. This helped me to visualise the "Things that were, things that are, and some things that have not yet come to pass." 
- It enabled me to track the progress of the project and make a plan that maximised efficiency and prioritised urgent tasks.
- This was essential in order to keep to a tight deadline.

---

## ⚙️ Set up

**Setting up Python:**
- I set up a virtual environment using venv and installed Requests and Rich.
- I created main.py and imported argparse, requests, random, and Console and Table from Rich.
- I also stored the base API URL as a variable.

---

## 🔧 Building the back-end

**Command-line arguments:**
- I used used argparse to ask the user which Pokémon they want to look-up, or if they want to generate a random Pokémon, or see a list of Pokémon from a specific type.
- I stored their response to be use a parameter for functions to fetch and display data about the Pokémon or type from the API.

**Fetch Pokémon by name or ID:**
- I used requests to call the PokéAPI by interpolating the name inputted by the user.
- I then utilised parse JSON to fetch the name, ID, types, base stats and sprite image URL.
- I added error handling to print a message to the user if they entered an invalid Pokémon name or ID.

**Display data:**
- I displayed the Pokémon data in a clean format using Rich tables.
- I printed a placeholder emoji, name, and ID. I will later display a specific emoji relevant to each type.
- I then printed the types and a URL link to the sprite image.
- Lastly, I created a table to display the base stats, with two columns for stat name and value. I used a for loop to add rows to the table for each base stat the value for that Pokémon.

**Count total Pokémon:**
- I dynamically fetched the PokéAPI “count” field from its list all Pokémon endpoint.
- This means the total number of Pokémon will automically update if more are added.
- I created a function to display the total of Pokémon.
- I can also use this to randomly select a Pokémon by ID.

**Feature: Random Pokémon:**
- I added a feature to return a random Pokémon.
- I added a --random flag, so when the user runs the script with --random, it will fetch a random Pokémon instead of requiring a name.
- I created a variable to generate a random ID between 1 and the total number of Pokémon.
- I then entered this as parameter when calling the get_pokemon_data function.

**Pokémon selection:**
- I used an ELIF statement to store the data for a random Pokémon unless the user requests a specific Pokémon. 
- I also added error handling to print a message to the user if they entered an invalid name.

**Feature: Type filter:**
- I added a feature to filter Pokémon by type.
- I had to work with multiple endpoints from the API, add the --type argument to my CLI, and create a function to list 20 Pokémon from that type using JSON. Using a for loop to print the Pokémon.
- I added error handling to print a message to the user if they entered an invalid type.

**Feature: Evolution chain:**
- I created a function to get the evolution chain for a Pokémon.
- I accessed the PokéAPI evolution-chain endpoint, through the species endpoint. Using API requests and JSON.
- I traversed the nested evolution chains recursively to collect names, then appended them to an array.
- I then called the function within my display_pokemon_info function. Using an if statement to join multiple evolutions with ' → '.

**Error handling:**
- I handled network failures (timeouts, connection errors, 404, 500).
- I checked for missing keys like "evolution_chain" or "chain".
- I printed user-friendly messages instead of crashing.
- The function safely returns an empty list when data isn’t available,  so the calling function can skip displaying it. 

**Dynamically Filter Valid IDs:**
- I encountered an error because my random Pokémon selector is using the total number of Pokémon returned by the API (get_total_pokemon()), but that count includes "forms" and "variants" that aren’t accessible by numeric ID; which means my app sometimes out-putted a random number like 1205 that doesn’t exist as a direct GET /pokemon/{id} resource.
- To be 100% API-driven, I fetched the full Pokémon list and picked a random name instead of random ID, that guarantees a valid Pokémon every time.

---

## 🎨 Styling the front-end

**Rich text styling:**
- I used Rich to make some of text bold or italic or change the font colour to add emphasis to key elements and improve the user experience.
- I also displayed the stats in a table to make it easier to read.

**Type-specific emojis:**
- To improve the user experience I displayed a different emoji for each type.
- I created a dictionary mapping Pokémon types to emojis using key:value pairs.
- I then created an empty array to store the list of types. Using a for loop I attached the correct emoji to each type, and appended it to the array.
- I added error handling to return ❓ if the type isn't in my dictionary.
- Lastly, I made a variable to store the concatenated, comma-separated string of a Pokémon's types with emojis.

---

## 🚀 Future plans

As this was a two day sprint and I am still learning Python, I had to prioritse the key user journey. Below is a list of features, improvements to the user experience and techical enhancements I would like to make in the future as I continue learning and progress my Python skills:

🏗 **New Features:**
- Interactive Mode – Let users select a Pokémon from a type list (e.g. choose 1–20) and immediately fetch its stats without rerunning the command.
- Multiple Pokémon Lookup – Allow passing multiple names at once (e.g. py main.py pikachu charizard) to compare stats.
- Stats Visualization – Use rich bar charts or ASCII graphs to visualize base stats instead of just numbers.
- Evolution Trigger Details – Show how each evolution happens (e.g. “Evolves at level 16” or “Use Water Stone”).
- Favorites System – Let users save favorite Pokémon to a local file (favorites.json) and list them later with --favorites.

🎨 **User Experience Improvements:**
- Better Error Messages – Suggest close matches if the user mistypes a Pokémon name (like a mini spellchecker).
- Color-Coded Stats – Use colors to highlight strong vs. weak stats (e.g. green for high Attack, red for low HP).
- Type Effectiveness Table – Show a mini chart of strengths/weaknesses when displaying a Pokémon.
- CLI Autocomplete (Advanced) – Add tab-completion for Pokémon names/types if running in an interactive shell.

🔧 **Technical Enhancements:**
- Test Coverage – Add unit tests for functions (e.g. get_evolution_chain, list_pokemon_by_type).
- Caching – Store recent API calls locally so repeated lookups are faster and work offline.
- Better Performance – Use asynchronous requests (httpx or aiohttp) to speed up multiple API calls (like when listing 20 Pokémon).
- Docker Support – Package the tool in a Docker container for easy setup on any system.
- Pre-Commit Hooks – Add black or flake8 to auto-format and lint code before commits.
