import json

base_stat_tiers = ["Legendary", "PseudoLegendary", "HighBST", "MidBST", "LowBST", "VeryLowBST"]
stat_tiers = ["LegendStat", "HighStat", "MidStat", "LowStat", "VeryLowStat"]
ou_cmp = ["AboveOU", "OU", "BelowOU"]
types = ["Normal", "Fire", "Water", "Grass", "Electric", "Ice", "Fighting", "Poison", "Ground", "Flying", "Psychic",
         "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
stats = ["hp", "atk", "def", "spa", "spd", "spe"]
all_abilities = []
all_moves = []

if __name__ == '__main__':
    with open("allmoves.json", "r") as f:
        all_moves = json.load(f)
    with open("allabilities.json", "r") as f:
        all_abilities = json.load(f)
    with open("allpokemon.json", "r") as f:
        with open("pokeparse_ou.txt", "w") as w, open('pokeparse_belowou.txt', 'w') as bou, open('pokeparse_aboveou.txt', 'w') as aou:
            w.write('@CONVERTED_FROM_TEXT\n')
            bou.write('@CONVERTED_FROM_TEXT\n')
            aou.write('@CONVERTED_FROM_TEXT\n')
            all_pokemon = json.load(f)
            counter = 1
            for x in types:
                w.write(f"@ITEM={counter}={x}\n")
                bou.write(f"@ITEM={counter}={x}\n")
                aou.write(f"@ITEM={counter}={x}\n")
                counter += 1
            for x in ou_cmp:
                w.write(f"@ITEM={counter}={x}\n")
                bou.write(f"@ITEM={counter}={x}\n")
                aou.write(f"@ITEM={counter}={x}\n")
                counter += 1
            for x in base_stat_tiers:
                w.write(f"@ITEM={counter}={x}\n")
                bou.write(f"@ITEM={counter}={x}\n")
                aou.write(f"@ITEM={counter}={x}\n")
                counter += 1
            for x in stats:
                for y in stat_tiers:
                    w.write(f"@ITEM={counter}={y}-{x}\n")
                    bou.write(f"@ITEM={counter}={y}-{x}\n")
                    aou.write(f"@ITEM={counter}={y}-{x}\n")
                    counter += 1
            for x in all_abilities:
                w.write(f"@ITEM={counter}={x}\n")
                bou.write(f"@ITEM={counter}={x}\n")
                aou.write(f"@ITEM={counter}={x}\n")
                counter += 1
            for x in all_moves:
                w.write(f"@ITEM={counter}={x}\n")
                bou.write(f"@ITEM={counter}={x}\n")
                aou.write(f"@ITEM={counter}={x}\n")
                counter += 1

            for p in all_pokemon:
                indexes = []
                index_len = 1

                # types
                for t in p.get("types"):
                    indexes.append(types.index(t) + index_len)
                index_len += len(types)

                # ou comparison
                # ou_cmp_val = ou_cmp.index(p.get('ou-cmp'))
                indexes.append(ou_cmp.index(p.get("ou-cmp")) + index_len)
                index_len += len(ou_cmp)

                # bst
                indexes.append(base_stat_tiers.index(p.get("bst-tier")) + index_len)
                index_len += len(base_stat_tiers)

                for s in stats:
                    stat = p.get(f"{s}-tier")
                    indexes.append(stat_tiers.index(stat) + index_len)
                    index_len += len(stat_tiers)

                for ability in p.get("abilities"):
                    indexes.append(all_abilities.index(ability) + index_len)
                index_len += len(all_abilities)

                for move in p.get("moves"):
                    indexes.append(all_moves.index(move) + index_len)
                index_len += len(all_moves)

                index_string = map(str, sorted(indexes))
                # print(index_string)
                # print(ou_cmp_val)
                ou_cmp_string = p.get('ou-cmp')
                # print(ou_cmp_string)
                if(ou_cmp_string == 'OU'):
                    w.write(f"{' '.join(index_string)}\n")
                elif(ou_cmp_string == 'BelowOU'):
                    bou.write(f"{' '.join(index_string)}\n")
                elif(ou_cmp_string == 'AboveOU'):
                    aou.write(f"{' '.join(index_string)}\n")
                
