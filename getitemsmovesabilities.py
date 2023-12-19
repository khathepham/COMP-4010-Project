import json

all_pokemon = set()
all_items = set()
all_moves = set()
all_abilities = set()

ag = json.load(open('gen9anythinggoes-0.json', 'r'))
ubers = json.load(open('gen9ubers-0.json', 'r'))
ou = json.load(open('gen9ou-0.json', 'r'))
uu = json.load(open('gen9uu-0.json', 'r'))
ru = json.load(open('gen9ru-0.json', 'r'))
nu = json.load(open('gen9nu-0.json', 'r'))
pu = json.load(open('gen9pu-0.json', 'r'))

# print(ou['data'].items())

for pokemon, v in ag['data'].items():
    # print(v['Items'])
    all_pokemon.add(pokemon)
    for item, usage in v["Items"].items():
        all_items.add(item)
    for move, usage in v['Moves'].items():
        all_moves.add(move)
    for ability, usage in v['Abilities'].items():
        all_abilities.add(ability)

for pokemon, v in ubers['data'].items():
    # print(v['Items'])
    all_pokemon.add(pokemon)
    for item, usage in v["Items"].items():
        all_items.add(item)
    for move, usage in v['Moves'].items():
        all_moves.add(move)
    for ability, usage in v['Abilities'].items():
        all_abilities.add(ability)

for pokemon, v in ou['data'].items():
    # print(v['Items'])
    all_pokemon.add(pokemon)
    for item, usage in v["Items"].items():
        all_items.add(item)
    for move, usage in v['Moves'].items():
        all_moves.add(move)
    for ability, usage in v['Abilities'].items():
        all_abilities.add(ability)
        if(pokemon == 'Eiscue'):
            print(ability)

for pokemon, v in uu['data'].items():
    # print(v['Items'])
    all_pokemon.add(pokemon)
    for item, usage in v["Items"].items():
        all_items.add(item)
    for move, usage in v['Moves'].items():
        all_moves.add(move)
    for ability, usage in v['Abilities'].items():
        all_abilities.add(ability)

for pokemon, v in ru['data'].items():
    # print(v['Items'])
    all_pokemon.add(pokemon)
    for item, usage in v["Items"].items():
        all_items.add(item)
    for move, usage in v['Moves'].items():
        all_moves.add(move)
    for ability, usage in v['Abilities'].items():
        all_abilities.add(ability)

for pokemon, v in nu['data'].items():
    # print(v['Items'])
    all_pokemon.add(pokemon)
    for item, usage in v["Items"].items():
        all_items.add(item)
    for move, usage in v['Moves'].items():
        all_moves.add(move)
    for ability, usage in v['Abilities'].items():
        all_abilities.add(ability)

for pokemon, v in pu['data'].items():
    # print(v['Items'])
    all_pokemon.add(pokemon)
    for item, usage in v["Items"].items():
        all_items.add(item)
    for move, usage in v['Moves'].items():
        all_moves.add(move)
    for ability, usage in v['Abilities'].items():
        all_abilities.add(ability)

# print(len(all_items))
# print(all_items)

# json.dump(sorted(all_pokemon), open("allpokemontest.json", "w"), indent=4)
json.dump(sorted(all_items), open("allitemsusage.json", "w"), indent=4)
json.dump(sorted(all_moves), open("allmovesusage.json", "w"), indent=4)
json.dump(sorted(all_abilities), open("allabilitiesusage.json", "w"), indent=4)

# with open('allitems.json', 'w') as f:
#     pass