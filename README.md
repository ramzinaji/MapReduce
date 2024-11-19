# MAPREDUCE

L'objectif de ce projet a été d'implémenter un algorithme world count disctribué sur plusieurs machine en utilisant le concept du mapreduce.

La fonction Map est la première étape de l'algorithme MapReduce. La phase Map travaille sur des paires de clés et de valeurs en entrée. Elle prend les tâches d'entrée et les divise en sous-tâches plus petites, puis effectue le calcul requis sur chaque sous-tâche en parallèle. La sortie du mappeur sera affichée sous la forme de paires (K,V). La phase de mappage effectue les deux sous-étapes suivantes -
1. **Splitting** - Prend l'ensemble de données d'entrée de la source et le divise en sous-ensembles de données plus petits.
2. **Mapping** - Prend les sous-ensembles de données plus petits en entrée et effectue l'action ou le calcul requis sur chaque sous-ensemble de données.
La sortie de la fonction Map est un ensemble de paires de clés et de valeurs sous la forme <Clé, Valeur>.

Après la phase de mapping , on effectue une tache de shuflle et reduce sur chaque machine en parallèle.
3. **Shuffle** - Prend les résulats de chauque map et on regroupe de les mots de même taille sur une même machine
4. **Reduce** - On regoupe les résultats de chaque machine sur un même dictionnaire et on addition les occurences des clés identiques

Dans ce projet, j'ai utilisé le fait que chaque machine avait un repertoire paratagé avec les autres machines de l'école pour éviter de faire des communications avec des sockets, je suis conscient que ce parti pris simplifie la tache mais l'objectif ici était de mettre en parralèle le ressources de plusieurs machines pour chaque étape du mapreduce.
