#!/usr/bin/env python3
import sys
import os
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# remove "." from paths when creating image for containers!!
def input(chunks):
    try:
        with open("../data/a-tale-of-two-cities.txt", encoding = 'utf-8') as mainfile:
            # d1 = mainfile.readline()
            line_count = file_len("../data/a-tale-of-two-cities.txt")
            chunk_size = int(line_count/chunks)
            for i in range(chunks):
                chunk_str = ""
                for j in range(chunk_size):
                    chunk_str+=mainfile.readline()  
                with open("../data/split_"+str(i+1)+"_"+str(chunks)+ ".txt","w", encoding = "utf-8") as chunk_file:
                    chunk_file.write(chunk_str)
        print("The data text file has been chunked into "+str(chunks)+" chunks (named spliti, 0<i<no_of_chunks)")
                
    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno,strerror))
        # print(sys.exc_type)

    # print(len("string"))
