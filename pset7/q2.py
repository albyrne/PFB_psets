import re
with open("python_07_nobody.txt","r") as f_read,open("albyrne.txt","w") as f_write:
	for line in f_read:
		newLine=line.rstrip()
		found=re.search(r"Nobody",newLine)
		if found:
			f_write.write(newLine.replace("Nobody","Albyrne"))
