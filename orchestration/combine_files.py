import glob

read_files = glob.glob("data/reduced/*.txt")

with open("data/final/final_text_freq.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())