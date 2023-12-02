import json
import requests
from Pokemon import Pokemon, Type, Tier, Category, Ability, Stats, Move

all_pokemon = []
all_abilities = {}
all_moves = {}


def get_all_pokemon() -> {}:
    f = open("gen9ou-1825.json")
    all_gen_9_pokemon = json.load(f)
    print(json.dumps(all_gen_9_pokemon["data"]["Iron Leaves"], indent=4))
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

        all_pokemon.append(p)

    print(all_pokemon[0])

if __name__ == '__main__':
    get_all_pokemon()
