import re
with open("python_07_nobody.txt","r") as f:
        count=0
        for line in f:
                count+=1
                print(str(count)+"\t"+line.strip())
