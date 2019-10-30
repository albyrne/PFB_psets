import re
with open("python_07.fasta","r") as f:
	for line in f:
		line=line.strip()
		match=re.search(r">(.+)\s",line)
		if match:	
			print(match.group(1))
			#goup1 specifies everything inside the parentheses	
