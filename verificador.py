import hashlib
import re

def hash(filename):
    with open(filename, "rb") as f:
        bytes = f.read()
        digest = hashlib.sha256(bytes).hexdigest()
    return digest

filename1 = input("Escribe el nombre del primer fichero: ")
filename2 = input("Escribe el nombre del segundo fichero: ")
with open(filename1,"r") as f:
    len1 = len(f.readlines())

with open(filename2, "r") as f:
    len2 = len(f.readlines())

if abs(len1-len2) != 1:
    print("NO")

else:
    if len2 > len1:
        ff = filename1
        filename1 = filename2
        filename2 = ff

        ll = len1
        len1 = len2
        len2 = ll
    
    same = True
    with open(filename1, "r") as f1:
        with open(filename2, "r") as f2:
            for ind,line2 in enumerate(f2):
                af = f1.readline()
                if line2 != af  and af != line2+"\n":
                    same = False
                    print("NO")
                    break

            if same and hash(filename1)[0] == "0" and re.search("[0-9a-z]{8}\t[0-9a-z]{2}\t100", f1.readline()):
                print("SI")
            else:
                print("NO")
