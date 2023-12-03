import json
import requests
from Pokemon import Pokemon, Type, Tier, Category, Ability, Stats, Move

all_pokemon = []
all_abilities = {}
all_moves = {}


def get_all_pokemon() -> {}:
    f = open("gen9ou-1825.json")
    all_gen_9_pokemon = json.load(f)
    # print(json.dumps(all_gen_9_pokemon["data"]["Iron Leaves"], indent=4))
    for k, v in all_gen_9_pokemon["data"].items():
        p = Pokemon(k)
        sum_abilities = 0
        for a, val in v["Abilities"].items():
            Ability(a)
            sum_abilities += val

        for a, val in v["Abilities"].items():
            p.abilities[a] = {"usage": val / sum_abilities, "reference": Ability.get_ability(a)}

        for m, val in v["Moves"].items():
            if m is not None and m != "":
                Move(m)
                usage = val / sum_abilities
                if usage > 0.03:
                    p.moves[m] = {"usage": val / sum_abilities, "reference": Move.get_move(m)}

        if v["usage"] >= 0.0454:
            p.tier = Tier.OU
        else:
            p.tier = Tier.BelowOU
        p.usage_rate = v["usage"]

        get_pokeapi(p)

        all_pokemon.append(p)

    print(all_pokemon[0])


def get_pokeapi(p: Pokemon):
    check_for_exception(p)
    pokemon_name = p.pokeapiname
    pokemon_name = pokemon_name.replace(" ", "-")
    pokemon_name = pokemon_name.lower()
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if r.status_code == 200:
        poke_data = r.json()
        #Get Stats
        for stat in poke_data["stats"]:
            val = stat["base_stat"]
            name = stat["stat"]["name"]
            match name:
                case "hp":
                    p.stats.hp = val
                case "attack":
                    p.stats.attack = val
                case "defense":
                    p.stats.defense = val
                case "special-attack":
                    p.stats.spattack = val
                case "special-defense":
                    p.stats.spdefense = val
                case "speed":
                    p.stats.speed = val
                case _:
                    print("Something Happened Getting Stats....")
        for t in poke_data["types"]:
            match t["slot"]:
                case 1:
                    p.primary_type = Type[t["type"]["name"].capitalize()]
                case 2:
                    p.secondary_type = Type[t["type"]["name"].capitalize()]
    else:
        print(f"Unable to get PokeApi Data for {p.name}.")
        print(f"Response Code: {r.status_code} {r.text}\n")

def check_for_exception(p: Pokemon):
    name = p.name
    if name in ("Tornadus", "Landorus", "Thundurus", "Enamorus"):
        p.pokeapiname = name + "-therian"
    elif "Tauros-Paldea" in name:
        p.pokeapiname = name + "-breed"
    elif name == "Toxtricity":
        p.pokeapiname = name + "-amped"
    elif name == "Indeedee":
        p.pokeapiname = name + "-male"
    elif name == "Indeedee-F":
        p.pokeapiname = "Indeedee-female"
    elif name == "Basculegion":
        p.pokeapiname = name + "-male"
    elif name == "Basculegion-F":
        p.pokeapiname = "Basculegion-female"
    elif name == "Mimikyu":
        p.pokeapiname = name + "-disguised"
    elif name == "Meloetta":
        p.pokeapiname = name + "aria"

if __name__ == '__main__':
    get_all_pokemon()
