# MAPREDUCE

L'objectif de ce projet a été d'implémenter un algorithme world count disctribué sur plusieurs machine en utilisant le concept du mapreduce.

La fonction Map est la première étape de l'algorithme MapReduce. La phase Map travaille sur des paires de clés et de valeurs en entrée. Elle prend les tâches d'entrée et les divise en sous-tâches plus petites, puis effectue le calcul requis sur chaque sous-tâche en parallèle. La sortie du mappeur sera affichée sous la forme de paires (K,V). La phase de mappage effectue les deux sous-étapes suivantes -
1. **Splitting** - Prend l'ensemble de données d'entrée de la source et le divise en sous-ensembles de données plus petits.
2. **Mapping** - Prend les sous-ensembles de données plus petits en entrée et effectue l'action ou le calcul requis sur chaque sous-ensemble de données.
La sortie de la fonction Map est un ensemble de paires de clés et de valeurs sous la forme <Clé, Valeur>.

Après la phase de mapping , on effectue une tache de shuflle et reduce sur chaque machine en parallèle.

3. **Shuffle** - Prend les résulats de chauque map et on regroupe de les mots de même taille sur une même machine
4. **Reduce** - On regoupe les résultats de chaque machine sur un même dictionnaire et on addition les occurences des clés identiques

Dans ce projet, j'ai choisi d'exploiter un répertoire partagé accessible à toutes les machines de l'école afin d'éviter les communications via des sockets. Bien que cette approche simplifie la tâche, l'objectif principal était de paralléliser les ressources de plusieurs machines à chaque étape du processus MapReduce.



J'ai utilisé trois structures intermédiaires pour stocker les données à chaque phase du traitement :

1. **mapped_i_n** : Ce fichier JSON contient les résultats du mapping pour le split de la machine i sur n. Chaque machine génère ce fichier à partir de son propre traitement des données.

2. **Global_dico_file_i** : Ce dictionnaire est organisé en sous-dictionnaires, chacun correspondant à une étape du shuffle. Pour remplir chaque sous-dictionnaire shuffle_k, on calcule le reste de la division euclidienne de la longueur du mot (len(mot)) par n. Si ce reste est égal à k, alors le mot est stocké dans le sous-dictionnaire shuffle_k. Ainsi, Global_dico_file_i a la structure suivante :

   Global_dico_file_i = { shuffle_1: {}, shuffle_2: {}, ..., shuffle_n: {}}
   Chaque sous-dictionnaire shuffle_k contient donc uniquement des mots dont la longueur est congruente à k modulo n (len(mot) % n == k).

4. **combine_global_dico** : Ce dictionnaire est également composé de n sous-dictionnaires. Cette fois, l'objectif est de fusionner les sous-dictionnaires shuffle_k intermédiaires provenant de chaque dictionnaire Global_dico_file_i pour toutes les machines i dans l'intervalle [1, n]. Cela permet de rassembler les résultats du shuffle de toutes les machines.

# Schéma du Système

cid:image001.png@01DB464A.B59A8AD0![image](https://github.com/user-attachments/assets/f1d6fcb9-d779-43ab-a8fb-896e56cde352)


# Comment exécuter 
Exécuter la commande ./run.sh

Entrer 3 pour le nombre de chunks

Si un mot de passe est demandé, la machine n'est pas disponible , utiliser une autre machine dans le fichier machines.txt

Parfois il est nécessaire de rexécuter le code run.sh plusieurs fois


