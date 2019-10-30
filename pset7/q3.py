import re
with open("python_07.fasta","r") as f:
	for line in f:
		line=line.rstrip()
		found=re.search(r">",line)
		if found:
		#	print(line)
			match=re.search(r">(\S+)",line)
			if match:
				print(match.group(1))
				#group1 specifies everything inside the parentheses

			#	startMatch=match.start()
			#	endMatch=match.end()
			#	print(line[startMatch:endMatch])
