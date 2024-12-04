import json

file_path = "../MapReduce/data/"
N=3

data={}

#Load the data
for i in range(N):
    path = file_path + 'Global_dico_part_' +str(i+1)+ '.json'
    with open(path, "r", encoding="utf-8") as f:
        data['machine_' + str(i+1)] = json.load(f) 

# Create the merge function for all the shuffle
def merge_dico(dico_1,dico_2):
    dico_merge={}
    for key in dico_1.keys():
        if key in dico_2.keys():
            dico_merge[key]=dico_1[key]+dico_2[key]
        else:
            dico_merge[key]=dico_1[key]
            
    for key in dico_2.keys():
        if key in dico_1.keys():
            dico_merge[key]= dico_merge[key]
        else:
            dico_merge[key]=dico_2[key]
            
    return dico_merge

def remove_first_key(d):
    d = dict(d)
    first_key = next(iter(d))
    d.pop(first_key)
    return d

def merge_n_dicts(data,k):
    top_machine=list(data.keys())[0]
    if len(list(data.keys())) == 1:
        return dicts[top_machine]['shuffle_'+k]
    data_new = remove_first_key(data)
    return merge2(data[top_machine]['shuffle_'+k], merge_n_dicts(data_new))

#Merged all the shuffles from all dictionaries into one dictionary. Normally, the result of each shuffle should be different due to the lengths of the words.
nbre_shuffle = N
merge={}
for k in range(N):
    merge.update(merge_dico(merge_dico(data['machine_1']['shuffle_' + str(k+1)],data['machine_2']['shuffle_'+ str(k+1)]),data['machine_3']['shuffle_'+ str(k+1)]))

# Sauvegarder le dictionnaire local de chaque machine dans un fichier JSON
with open(f"../MapReduce/data/merged_global_dico.json", "w", encoding="utf-8") as f:
    json.dump(merge, f)