#!/usr/bin/env python3
import sys
output_no = sys.argv[1]
total_chunks = sys.argv[2]
print(output_no)
data_location = "MapReduce/data/"
input_file_path = data_location+"split_"+str(output_no)+"_"+str(total_chunks)+".txt"
mapped_dict = {}
try:

    with open(input_file_path, encoding = 'utf-8') as f:
        d = f.read()
        l = d.split(" ")
        for x in l:
                if x not in mapped_dict:
                    mapped_dict[x] = 1
                else:
                    mapped_dict[x] = mapped_dict[x] + 1
        with open(data_location+"mapped_"+str(output_no)+"_"+str(total_chunks)+ ".txt","w", encoding = "utf-8") as mapped_data_file:
            tup_view = mapped_dict.items()
            tup_list = list(tup_view)
            for y in tup_list:
                mapped_data_file.write(str(y)+"\n")
            
                
except IOError as e:
    print(IOError,e)