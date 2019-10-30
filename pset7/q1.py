import re
with open("enumerated_poem.txt","r") as f:
	for line in f:	
		newLine=line.rstrip()
		fields=newLine.split("\t")
		if len(fields) > 1:
			found=re.search(r"Nobody",fields[1])
			if found:
				start=found.start()+1
				end=found.end()
				print("Line:",fields[0],"Nobody is in positions [" +str(start)+ ":" +str(end)+ "]")

		
