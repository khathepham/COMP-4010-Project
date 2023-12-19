import json
import threading

formats = ["AG", "Uber", "OU", "UUBL", "UU", "RUBL", "RU", "PUBL", "PU", "NUBL", "NU", "ZUBL", "ZU"]
ou_cmp = ["AboveOU", "OU", "BelowOU"]
types = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic",
         "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
base_stat_tiers = ["Legendary", "PseudoLegendary", "HighBST", "MidBST", "LowBST", "VeryLowBST"]
stat_tiers = ["LegendStat", "HighStat", "MidStat", "LowStat", "VeryLowStat"]

ag = json.load(open('gen9anythinggoes-0.json', 'r'))
ubers = json.load(open('gen9ubers-0.json', 'r'))
ou = json.load(open('gen9ou-0.json', 'r'))
# uu = json.load(open('gen9uu-0.json', 'r'))
# ru = json.load(open('gen9ru-0.json', 'r'))
# nu = json.load(open('gen9nu-0.json', 'r'))
# pu = json.load(open('gen9pu-0.json', 'r'))

def get_pokemon():
    # print(ou['data']['Iron Leaves'])
    with open("allmoves.json", "r") as f:
        global all_moves
        all_moves = json.load(f)

    with open("pokejson.json", "r") as f:
        all_data = json.load(f)
        all_pokemon = all_data["injectRpcs"][1][1]['pokemon']
        valid_pokemon = []

        threads = []
        for p in all_pokemon:
            t = threading.Thread(target=do_the_things(p, valid_pokemon))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        json.dump(valid_pokemon, open("allpokemonusage.json", "w"), indent=4)
        # print(json.dumps(valid_pokemon[0], indent=4))

def do_the_things(p, valid_pokemon):
    in_tier = len(set(formats) & set(p["formats"]))
    if in_tier != 0 and p["oob"] is not None and len(p.get("alts", [])) == 0 and "SV" in p.get("oob").get("genfamily"):
        p.pop("height")
        p.pop("weight")
        p.pop("oob")
        add_bst(p)
        success = False
        if(p['formats'][0] == 'Uber'):
            success = add_moves_and_items(p, ubers)
        else:
            success = add_moves_and_items(p, ou)
            
        if(success):
            if p.get("formats")[0] in formats[0:2]:
                p["ou-cmp"] = "AboveOU"
            elif p.get("formats")[0] == formats[2]:
                p["ou-cmp"] = "OU"
            else:
                p["ou-cmp"] = "BelowOU"

            valid_pokemon.append(p)

def add_moves_and_items(p, tier_data):
    # print(tier_data['info'])
    success = True
    moves = []
    items = []
    abilities = []
    # print(p['formats'][0])
    # print(p['name'])
    if(p['name'] in tier_data['data']):
        total = 0
        for k, v in tier_data['data'][p['name']]['Abilities'].items():
            abilities.append(k)
            total += v

        for k, v in tier_data['data'][p['name']]['Moves'].items():
            if((v / total) > 0.05):
                moves.append(k)
        
        for k, v in tier_data['data'][p['name']]['Items'].items():
            if((v / total) > 0.05):
                items.append(k)

    else:
        print(p['name'] + ' was not found in the data')
        success = False
    p['abilities'] = abilities
    p['moves'] = moves
    p['items'] = items

    return success

def add_bst(p):
    stats = ["hp", "atk", "def", "spa", "spd", "spe"]
    bst = 0
    bst_tier = base_stat_tiers[-1]
    for s in stats:
        stat = int(p.get(s))
        stat_level = stat_tiers[-1]
        if stat >= 150:
            stat_level = stat_tiers[0]
        elif stat >= 125:
            stat_level = stat_tiers[1]
        elif stat >= 100:
            stat_level = stat_tiers[2]
        elif stat >= 85:
            stat_level = stat_tiers[3]
        p[f"{s}-tier"] = stat_level
        bst += stat

    if bst > 600:
        bst_tier = base_stat_tiers[0]
    elif bst == 600:
        bst_tier = base_stat_tiers[1]
    elif bst >= 550:
        bst_tier = base_stat_tiers[2]
    elif bst >= 500:
        bst_tier = base_stat_tiers[3]
    elif bst >= 450:
        bst_tier = base_stat_tiers[4]

    p["bst-tier"] = bst_tier

if __name__ == '__main__':
    get_pokemon()
