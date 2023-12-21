Setup
===
Make sure all files within the package are in the same directory  
Run getitemsmovesabilities.py file to generate a json files containing the Pokemon moves, items, and abilties  
Run usagegetpokemon.py to generate a json file that contains every Pokemon along with their characteristics  
Run pokemon_to_separate_tiers.py to generate txt files that can be used as input for the spmf.jar file  
pokeparse_ou.txt contains only Pokemon within the OU tier, pokeparse_belowou.txt contains only Pokemon below the OU tier, pokeparse_above contains only Pokemon above the OU tier, and pokeparse_all contains all Pokemon within the dataset  

Frequent Pattern and Association Rule Mining
===
Run the spmf.jar file to launch a gui to perform frequent pattern and association rule mining
To perform closed frequent pattern mining, choose the algorithm FPClose found under Frequent Itemset Mining  
To perform association rule mining, choose the algorithm Closed_association_rules(using_fpclose) found under Association Rule Mining
For the input select any of the generated pokeparse.txt files  
The output can be any txt file  
Set the desired minsup and minconf then click on run algorithm to run the algorithm  


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