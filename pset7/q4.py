import re
with open("python_07.fasta","r") as f:
	for line in f:
		line=line.strip()
		match1=re.search(r">(.+?)\s",line)
		#match2=re.search(r">.+\s(.+)\n",line)	
		if match1:
			startMatch=match1.start()
			endMatch=match1.end()
			print("ID:",match1.group(1))
			match2=re.search(r">.+\s(.+)\n",line)
			if match2:
				print("Description:",match2.group(1))
