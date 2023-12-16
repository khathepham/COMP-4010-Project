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


def filter_rules_in_tier(input, output, tier):
    count=0
    with open(input, "r") as f:
        fout=open(output, "w")
        for line in f:
            tokens=line.split(' ')
            if tier in tokens:
                fout.write(line)
                count=count+1
                
                
    print(f"There are {count} number of association rules that involve {tier}")
                
        


if __name__ == '__main__':
    make_look_up_table("pokeparsetest.txt")
    convert_ids_to_strings("output_inverse_rules_in_string.txt", "output_inverse_rules.txt")
    filter_rules_in_tier("output_inverse_rules_in_string.txt", "output_inverse_ou.txt", "OU")
    filter_rules_in_tier("output_inverse_rules_in_string.txt", "output_inverse_above_ou.txt", "AboveOU")
    filter_rules_in_tier("output_inverse_rules_in_string.txt", "output_inverse_above_ou.txt", "BelowOU")
    
    
    



    

    

                    

            
            
        
        