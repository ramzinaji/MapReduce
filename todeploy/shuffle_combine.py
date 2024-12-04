import sys
from ast import literal_eval as make_tuple
import json

# Récupération de l'index de la machine pour le nom de fichier
index = int(sys.argv[1])# L'index passé en argument pour identifier la machine
N = int(sys.argv[2])  # Nombre de machines / Dictionnaires globaux
input_file_path = f"/cal/exterieurs/rnaji-24/MapReduce/data/mapped_{index}_3.txt"


Global_dico = {f'shuffle_{i + 1}': {} for i in range(N)}

print("Processing file:", input_file_path)

with open(input_file_path, encoding='utf-8') as f:
    d = f.read()
    tuples_list = d.split("\n")
    
    for j_tuple in tuples_list:
        try:
            j_tuple = make_tuple(j_tuple)
            word, count = j_tuple[0], j_tuple[1]
            
            # Assigner le mot au bon dictionnaire basé sur sa longueur
            dict_key = f"shuffle_{(len(word) % N) + 1}"
            #print(f"{word} (len={len(word)}) goes to {dict_key}")
            
            # Ajouter le mot dans le dictionnaire approprié
            if word not in Global_dico[dict_key]:
                Global_dico[dict_key][word] = count
            else:
                Global_dico[dict_key][word] += count
                
        except Exception as e:
            print("Error processing tuple:", j_tuple, "| Exception:", e)



# Sauvegarder le dictionnaire local de chaque machine dans un fichier JSON
with open(f"/cal/exterieurs/rnaji-24/MapReduce/data/Global_dico_part_{index}.json", "w", encoding="utf-8") as f:
    json.dump(Global_dico, f)



