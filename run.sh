#!/bin/bash

# Commence le chronométrage
START_TIME=$(ruby -e 'puts (Time.now.to_f * 1000).to_i')

# Variables
login="rnaji-24"
localFolder="./"
todeploy="MapReducePython/todeploy"
deployed="todeploy"
remoteFolder="mapreducedeployed"
nameOfTheScript_map="map_local.py"
nameOfTheScript_reduce="reduce_local.py"
dataFolder="MapReducePython"

# Lire les machines depuis le fichier machines.txt et les mettre dans un tableau
machines=($(cat machines.txt))

# Commande pour exécuter le script à distance sur la première machine (création du dossier)
command1=("ssh" "-tt" "$login@${machines[0]}" "rm -rf $remoteFolder; mkdir $remoteFolder")

# Exécution de la commande SSH sur la première machine
echo "Running command: ${command1[*]}"
"${command1[@]}"

echo "$(pwd)"
cd ..

# Copie du dossier à déployer sur la première machine
command2=("scp" "-r" "$localFolder$todeploy" "$login@${machines[0]}:$remoteFolder")
echo "Running command: ${command2[*]}"
"${command2[@]}"

# Début de la simulation MapReduce
echo "----------------------- INITIALISING MAPREDUCE SIMULATION ---------------------\n\n"

echo "ENTER THE NUMBER OF AVAILABLE NODES: "
read chunks

# Phase de chunking
echo "------------- INITIALISING CHUNKING SCRIPT OF INPUT TEXT FILE -------------\n"
echo "$(pwd)"
cd MapReducePython/orchestration
echo "$(ls)"
python3 main.py $chunks
cd ..

echo "------------- TERMINATING CHUNKING SCRIPT OF INPUT TEXT FILE -------------\n"

# Phase de Map
echo "------------- INITIALISING MAP PHASE -------------\n"


# Lancer les conteneurs en parallèle pour la phase Map
for i in "${!machines[@]}"
do
    # Machine courante
    machine="${machines[$i]}"
    echo "Index: $i, Machine: $machine"
    echo "$(pwd)"
    # Commande SSH pour exécuter le script Map sur la machine
    i=$((i + 1))
    command3=("ssh" "-tt" "$login@$machine" " python3 $remoteFolder/$deployed/$nameOfTheScript_map $i $chunks")
    echo "Running command: ${command3[@]}"  # Affiche la commande pour débogage
    
    # Exécution en parallèle
    "${command3[@]}" &
done

# Attendre que toutes les tâches Map en parallèle soient terminées
wait

# # Phase Combine
# echo "------------- INTERMEDIATE COMBINE PHASE INITIATION IN PARALLEL-------------\n"

# # Exécuter le script de combinaison localement
# python3 combine/combine_local.py $chunks

echo "------------- SHUFFLE PHASE IN PARALLEL-------------\n"

# Exécuter le script de combinaison localement
file="machines.txt"
machines_list=$(tr '\n' ',' < "$file" | sed 's/,$//')

python3 todeploy/run_shuffle_combine.py "$login" "$machines_list"

echo "------------- MERGE -------------\n"

python3 todeploy/merge_shuflled.py


echo "----------------------- TERMINATING MAPREDUCE SIMULATION ---------------------\n\n"

# Calcul du temps de calcul total
END_TIME=$(ruby -e 'puts (Time.now.to_f * 1000).to_i')
COMP_TIME=$((END_TIME - START_TIME))
echo "****TOTAL COMPUTATION TIME OF THE ALGORITHM: $COMP_TIME ms ****"

# Attendre la fin des processus parallèles
wait
