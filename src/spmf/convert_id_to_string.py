import sys


look_up_table={}



def make_look_up_table(dict):
        with open(dict, "r") as f:
     
            for line in f:
                line=line.rstrip('\n')
                
                if line[0]=='@':
                    tokens=line.split('=')


                    tokens[2]=tokens[2].replace(" ", "_")
                    look_up_table[int(tokens[1])]=tokens[2]
                else:
                    break


def convert_ids_to_strings(output,input):
    with open(output, "w") as f:
        input =open(input, "r")
        for line in input:
            tokens=line.split(" ")
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


def extract_rules(set):
    rules=[]
    for line in set:
        sup_index=line.find("#SUP")
        rules.append(line[:sup_index]+"\n")

    return rules


def filter_rules_in_tier(input, output, tier):
    
    rules={}
    rules_frozen={}
    index=0
    with open(input, "r") as f:
        fout=open(output, "w")
        for line in f:
            tokens=line.strip().split(' ')
            tokens_frozen=frozenset(tokens)
           # if tier in tokens:
            if tokens_frozen not in rules_frozen.values():
                #if index<10:
                #    print(f"Line: {line.strip()}\n\t, Tokens: {tokens}\n\t, Rules: {rules.values()}")
                rules[index]=line
                rules_frozen[index]=tokens_frozen
                index=index+1
                
        count=0       
        for i in rules.keys():
                #fout.write(str(rules[i])+"\n")
                fout.write(rules[i])
                if tier in rules.values():
                     count=count+1
    
                
    print(f"There are {count} number of association rules that involve {tier}")
    print(f"There are {len(rules.keys())} distinguishable rules in {tier}\n")

    return rules.values()
    
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
    
                
ALL_POKES="pokeparse.txt"
OU_POKES="pokeparse_ou.txt"
ABOVE_OU_POKES="pokeparse_aboveou.txt"  
BELOW_OU_POKES="pokeparse_belowou.txt"


if __name__ == '__main__':
    #finput=sys.argv[1]
    #print(finput)
    make_look_up_table("pokeparsetest.txt")
    #if finput==ALL_POKES:
        #pass
    #elif finput==OU_POKES:
    convert_ids_to_strings("output_inverse_rules_in_string_ou.txt", "output_ou_inverse_rules_ID.txt")
    ou_rules=filter_rules_in_tier("output_inverse_rules_in_string_ou.txt", "output_disting_rules_inverse_ou.txt", "OU")
    ou_rules=extract_rules(ou_rules)
   # elif finput==ABOVE_OU_POKES:
    convert_ids_to_strings("output_inverse_rules_in_string_above_ou.txt", "output_above_ou_inverse_rules_ID.txt")
    above_ou_ruls=filter_rules_in_tier("output_inverse_rules_in_string_above_ou.txt", "output_disting_rules_inverse_above_ou.txt", "AboveOU")
    above_ou_ruls=extract_rules(above_ou_ruls)
    #elif finput==BELOW_OU_POKES:
    convert_ids_to_strings("output_inverse_rules_in_string_below_ou.txt", "output_below_ou_inverse_rules_ID.txt")
    below_ou_rules=filter_rules_in_tier("output_inverse_rules_in_string_below_ou.txt", "output_disting_rules_inverse_below_ou.txt", "BelowOU")
    below_ou_rules=extract_rules(below_ou_rules)
    
    sets=[ou_rules, above_ou_ruls, below_ou_rules]
    
    overlapping_rules=find_overlapping_rules(sets)
    above_below_rules=[above_ou_ruls, below_ou_rules]
    union_rules=find_union_rules(above_below_rules)
    
    
    
    print(f"There are {len(overlapping_rules)} different rules in intersection.")    
    print(f"There are {len(union_rules)} different rules in above and below union.")
    
    ou_complement=find_special_rules_only_in_ou(ou_rules, union_rules)
    
    
    
    



    

    

                    

            
            
        
        