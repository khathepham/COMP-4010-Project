from efficient_apriori import apriori

transactions = [('eggs', 'bacon', 'soup', 'rice'),
                ('eggs', 'bacon', 'apple', 'rice'),
                ('soup', 'bacon', 'banana', 'rice')]
transactions=[]
with open("pokeparse_ou.txt","r") as f:
  for line in f:
    if line[0]!="@":
      tokens =line.split(' ')
      transactions.append(set(tokens))

      
      
itemsets, rules = apriori(transactions, min_support=0.1, min_confidence=1)
count=0
# Print out every rule with 2 items on the left hand side,
# 1 item on the right hand side, sorted by lift
rules_rhs = filter(lambda rule: len(rule.lhs) == 500 and len(rule.rhs) == 500, rules)
with open("output_python.txt", "w") as f:
  for rule in sorted(rules_rhs, key=lambda rule: rule.lift):
    f.write(f"{rule}\n")  # Prints the rule and its confidence, support, lift, ...
    count=count+1
    
print(f"Numbe rof rules {count}")