import paramiko
import threading
import sys

user = sys.argv[1]
hosts = sys.argv[2].split(",")

hosts = [{"host":host,"user":user,"index":i+1}  for i,host in enumerate(hosts)]


port = 22
mdp = 'Fixiegear_2000@RN!'

N=3
def run_script_on_remote(host, user, index):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host,port=port,username=user,password= mdp)
    
    # Commande pour exécuter process_data.py sur la machine distante
    command = f"python3 /cal/exterieurs/rnaji-24/MapReduce/todeploy/shuffle_combine.py {index} {N}"
    ssh.exec_command(command)
    ssh.close()
    print(f"Script lancé sur {host}")

threads = []
for host_info in hosts:
    t = threading.Thread(target=run_script_on_remote, args=(host_info["host"], host_info["user"], host_info["index"]))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Tous les scripts distants ont été lancés.")
