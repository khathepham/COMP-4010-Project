Setup
===
Make sure all files within the package are in the same directory  
Run getitemsmovesabilities.py file to generate a json files containing the Pokemon moves, items, and abilties  
Run usagegetpokemon.py to generate a json file that contains every Pokemon along with their characteristics  
Run pokemon_to_separate_tiers.py to generate txt files that can be used as input for the spmf.jar file  
pokeparse_ou.txt contains only Pokemon within the OU tier, pokeparse_belowou.txt contains only Pokemon below the OU tier, pokeparse_above contains only Pokemon above the OU tier, and pokeparse_all contains all Pokemon within the dataset  

Frequent Pattern and Association Rule Mining
===

Run the spmf.jar file to launch a gui to perform FP close frequent pattern and association closed rule using FP close mining

To perform closed frequent pattern mining, choose the algorithm FPClose found under Frequent Itemset Mining. Set the desire minsup and name output file as wanted.

To perform association rule mining:
+ Choose the algorithm Closed_association_rules(using_fpclose) found under Association Rule Mining
+ For the input select any of the generated pokeparse.txt files. e.g: pokeparse_all.txt for the dataset of all Pokemon, pokeparse_ou for the dataset only includes OU Pokemon, and similarly to pokeparse_aboveou.txt and pokeparse_belowou.txt
+ The output can be any txt file  
+ Set the desired minsup and minconf then click on run algorithm to run the algorithm  

To perform Association closed rules with Apriori Inverse:
+ Go to src/spmf
+ Compile javac MainTestAllAssociationRules_AprioriInverse_saveToFile_withLift.java
+ Run ```java MainTestAllAssociationRules_AprioriInverse_saveToFile_withLift input_file_name minsup_value maxsup_value minconf_value min_lift_value output_1.txt```
, for example: if we want to run the association closed perfect rare rules with minsup=0.004, maxsup=0.1, minconf=0.5 and minlift=1 on our entire dataset, we use:
```
java MainTestAllAssociationRules_AprioriInverse_saveToFile_withLift pokeparse_all.txt 0.004 0.1 0.5 1 output_1.txt
```
+ Since output is saved in output file is in ID, run ```python3 convert_id_to_string_simple.py``` to see the results in strings. The output is saved in output_final (for the entire output), output_final_ou.txt (for the rules in OU), similarly for output_final_aboveou.txt and output_final_belowou.txt. Note: output_patterns_string.txt is the output of the apriori inverse frequent items in string. 



Datasets
===
https://www.smogon.com/dex/sv/pokemon/  
https://www.smogon.com/stats/2023-11/chaos  
https://www.smogon.com/stats/2023-11/chaos/gen9anythinggoes-0.json   
https://www.smogon.com/stats/2023-11/chaos/gen9ubers-0.json  
https://www.smogon.com/stats/2023-11/chaos/gen9ou-0.json  
https://www.smogon.com/stats/2023-11/chaos/gen9uu-0.json  
https://www.smogon.com/stats/2023-11/chaos/gen9ru-0.json  
https://www.smogon.com/stats/2023-11/chaos/gen9nu-0.json  
https://www.smogon.com/stats/2023-11/chaos/gen9pu-0.json  