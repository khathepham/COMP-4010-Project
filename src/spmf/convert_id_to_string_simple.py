import json
import sys


look_up_table={}
all_moves=[]
all_abilities=[]
all_tiers=[]
all_types=[]


def make_look_up_table(dict):
        with open(dict, "r") as f:
     
            for line in f:
                line=line.rstrip('\n')
                
                if line[0]=='@':
                    tokens=line.split('=')
                    if len(tokens)>=2:


                        tokens[2]=tokens[2].replace(" ", "_")
                        look_up_table[int(tokens[1])]=tokens[2]
                else:
                    break


def category_dictionary():
    
    with open("allmovesusage.json", "r") as f:
        global all_moves
        all_moves=json.load(f)
    with open("allabilitiesusage.json", "r") as f: 
        global all_abilities 
        all_abilities=json.load(f)
    with open("alltiers.json", "r") as f:
        global all_tiers
        all_tiers=json.load(f)
        
    with open("alltypes.json", "r") as f:
        global all_types
        all_types=json.load(f)
        


def convert_ids_to_strings(output,input):
    category_dictionary()
    #print(all_moves)
    with open(output, "w") as f:
        input =open(input, "r")
        for line in input:
            line=line.rstrip('\n')
            tokens=line.split(" ")
            #print(tokens)
            i=0
            notId=False
            for i in range(len(tokens)):
                if not notId and tokens[i].isdigit():
                        f.write(' '+look_up_table[int(tokens[i])])
                elif tokens[i]=='==>':
                        f.write(' '+tokens[i])
                elif tokens[i]=='#SUP:':
                      f.write(' '+tokens[i])
                      notId=True
                else:
                    f.write(' '+tokens[i])
            f.write("\n")


def extract_rules(set):
    rules=[]
    for line in set:
        sup_index=line.find("#SUP")
        rules.append(line[:sup_index]+"\n")

    return rules


def filter_rules_in_tier(input, output, tier):
    
    rules=set()
    tier_ou="tier:OU"
    tier_aboveou="tier:AboveOU"
    tier_belowou="tier:BelowOU"
 
    count_ou=0
    count_aboveou=0
    count_belowou=0
    with open(input, "r") as f:
        fout=open(output, "w")
        fout_ou=open(output+"_ou.txt" , "w")
        fout_aboveou=open(output+"_aboveou.txt", "w")
        fout_belowou=open(output+"_belowou.txt", "w")
        for line in f:
                tokens=line.strip().split(' ')
                rules.add(line)
                fout.write(line)
                if tier_ou in tokens:
                    fout_ou.write(line)
                    count_ou=count_ou+1
                if tier_aboveou in tokens:
                    fout_aboveou.write(line)
                    count_aboveou=count_aboveou+1
                if tier_belowou in tokens:
                    fout_belowou.write(line)
                    count_belowou=count_belowou+1
                    
    
                
    print(f"There are {count_ou} number of association rules that involve {tier_ou}")
    print(f"There are {count_aboveou} number of association rules that involve {tier_aboveou}")
    print(f"There are {count_belowou} number of association rules that involve {tier_belowou}")
    print(f"There are {len(rules)} distinguishable rules in...\n")

    return rules
    
def find_overlapping_rules(sets):
    sets_frozen=[]
    map_frozenset_rule={}
    for i in range(len(sets)):
        
        set_frozen={frozenset(item.strip().split(' ')) for item in sets[i]}
        
        for rule in sets[i]:
            rule_frozen=frozenset(rule.strip().split(' '))
            map_frozenset_rule[rule_frozen]=rule
        
        sets_frozen.append(set_frozen)
                
    overlap_frozen=set.intersection(*sets_frozen)
    
    overlap=[]
    for rule_frozen in overlap_frozen:
        overlap.append(map_frozenset_rule[rule_frozen])
    
    overlap=sorted(overlap)
        
    with open("output_intersection.txt", "w") as f:
        for rule in overlap:
            f.write(rule)
    return overlap
        


def find_union_rules(sets):
    sets_frozen=[]
    map_frozenset_rule={}
    for i in range(len(sets)):
        
        set_frozen={frozenset(item.strip().split(' ')) for item in sets[i]}
        
        for rule in sets[i]:
            rule_frozen=frozenset(rule.strip().split(' '))
            map_frozenset_rule[rule_frozen]=rule
        
        sets_frozen.append(set_frozen)
        
    union_frozen=set.union(*sets_frozen)
    
    union=[]
    for rule_frozen in union_frozen:
        union.append(map_frozenset_rule[rule_frozen])
    
    union=sorted(union)
    with open("output_union.txt", "w") as f:
        for rule in union:
            f.write(rule)
    
    return union
        
        

def find_special_rules_only_in_ou(ou_set, union):
    union_set_frozen=[]
    map_frozenset_rule={}
    for rule in union: 
            rule_frozen=frozenset(rule.strip().split(' '))
            map_frozenset_rule[rule_frozen]=rule
            union_set_frozen.append(rule_frozen)
    
    ou_set_frozen=[]
    for rule in ou_set:
            rule_frozen=frozenset(rule.strip().split(' '))
            map_frozenset_rule[rule_frozen]=rule
            ou_set_frozen.append(rule_frozen)
        
        
    ou_complement_frozen=set(ou_set_frozen) - set(union_set_frozen)
    
    ou_complement=[]
    for rule_frozen in ou_complement_frozen:
        ou_complement.append(map_frozenset_rule[rule_frozen])
    
    ou_complement=sorted(ou_complement)
    with open("output_complement.txt", "w") as f:
        for rule in ou_complement:
            f.write(rule)
        
    
    print(f"There are {len(ou_complement)} different rules in ou_complment.")  
    return ou_complement
    



if __name__ == '__main__':
    #finput=sys.argv[1]
    #print(finput)
    make_look_up_table("pokeparse_all.txt")
    #if finput==ALL_POKES:
        #pass
    #elif finput==OU_POKES:
    convert_ids_to_strings("output_patterns_string.txt", "output_patterns_id.txt")
    convert_ids_to_strings("output_intermediate.txt", "output_1.txt")
    all_rules=filter_rules_in_tier("output_intermediate.txt", "ouput_final", "OU")

    
    
    
    



    

    

                    

            
            
        
        