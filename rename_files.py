import os  

#Change folder directory
os.chdir(r"<folder directory>")
cd = os.getcwd()

i = 1

for filename in os.listdir(cd):
    if filename.startswith("<Title>"):
        os.rename(filename, "<Title ep. > " + str(i) + ".<file format type>")
        i += 1

