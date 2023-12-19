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


                    tokens[2]=tokens[2].replace(" ", "_")
                    look_up_table[int(tokens[1])]=tokens[2]
                else:
                    break

def category_dictionary():
    
    with open("allmoves.json", "r") as f:
        global all_moves
        all_moves=json.load(f)
    with open("allabilities.json", "r") as f: 
        global all_abilities 
        all_abilities=json.load(f)
    with open("alltiers.json", "r") as f:
        global all_tiers
        all_tiers=json.load(f)
        
    with open("alltypes.json", "r") as f:
        global all_types
        all_types=json.load(f)
    
def category_of(tokens):

    if tokens in all_moves:
        return "move:"
    if tokens in all_abilities:
        return "abilities:"
    if tokens in all_tiers:
        return "tier:"
    if tokens in all_types:
        return "type:"
    else:
        return "something_else:"

def convert_ids_to_strings(output,input):
    category_dictionary()
    with open(output, "w") as f:
        input =open(input, "r")
        for line in input:
            tokens=line.split(" ")
            #print(tokens)
            i=0
            notId=False
            for i in range(len(tokens)):
                if not notId and tokens[i].isdigit():
                        f.write(' '+category_of(look_up_table[int(tokens[i])])+look_up_table[int(tokens[i])])
                elif tokens[i]=='==>':
                        f.write(' '+tokens[i])
                elif tokens[i]=='#SUP:':
                      f.write(' '+tokens[i])
                      notId=True
                else:
                    f.write(' '+tokens[i])


def extract_rules(my_set):
    rules=set()
    for line in my_set:
        sup_index=line.find("#SUP")
        rules.add(line[:sup_index]+"\n")

    return rules


def filter_rules_in_tier(input, output, tier):
    
    rules=set()
 
    count=0
    with open(input, "r") as f:
        fout=open(output, "w")
        for line in f:
                tokens=line.strip().split(' ')
                rules.add(line)
                fout.write(line)
                if tier in tokens:
                     count=count+1
    
                
    print(f"There are {count} number of association rules that involve {tier}")
    print(f"There are {len(rules)} distinguishable rules in {tier}\n")

    return rules
    
def find_overlapping_rules(sets):

    overlap=set.intersection(*sets)
    
    overlap=sorted(overlap)
        
    with open("output_intersection.txt", "w") as f:
        for rule in overlap:
            f.write(rule)
    return overlap
        


def find_union_rules(sets):

        
    union=set.union(*sets)
    
    union=sorted(union)
    with open("output_union.txt", "w") as f:
        for rule in union:
            f.write(rule)
    
    return union
        
        

def find_special_rules_only_in_ou(ou_set, union):
        
        
    ou_complement=set(ou_set) - set(union)

    
    ou_complement=sorted(ou_complement)
    with open("output_complement.txt", "w") as f:
        for rule in ou_complement:
            f.write(rule)
        
    
    print(f"There are {len(ou_complement)} different rules in ou_complment (ou only).")  
    return ou_complement
    
         
         
def find_maximum_rules(rules,set_name):
    rules=sorted(rules, reverse=True)
    rules_split=set()
    for rule in rules:
        rule_splitting=rule.strip().split('==>')
        rules_split.add((tuple(set((rule_splitting[0].strip().split(' ')))),tuple(set(rule_splitting[1].strip().split(' ')))))
        
        
        
    maximum=set()
    rules_split=sorted(rules_split, key=lambda x: (len(x[0]), len(x[1]),x[0], x[1] ), reverse=True)
    
    with open("ouput_maximum_rules_"+set_name+".txt", "w") as f:
        for antecedent, consequent in rules_split:
            if any(set(antecedent).issubset(item[0]) and set(consequent).issubset(item[1]) for item in maximum):
                pass
            else:
                maximum.add((antecedent,consequent))
                f.write(f"{ ' '.join(map(str, antecedent))} ==> { ' '.join(map(str, consequent))}\n")
    
    print(f"There are {len(maximum)} number of maximum rules in {set_name}")
    
    return maximum
            

       
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
    union_all=find_union_rules(sets)
    
    
    
    print(f"There are {len(overlapping_rules)} different rules in intersection.")    
    print(f"There are {len(union_rules)} different rules in above and below union.")
    print(f"There are {len(union_all)} different rules in 3 tiers union.")
    
    ou_complement=find_special_rules_only_in_ou(ou_rules, union_rules)
    
    maximum_ou=find_maximum_rules(ou_complement, "ou_complement")
    
    
    



    

    

                    

            
            
        
        