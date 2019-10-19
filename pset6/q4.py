with open("python_06.fastq","r") as f_read:
	lineCount=0
	charCount=0
	for line in f_read:
		lineCount+=1
		for char in line:
			charCount+=1
		#	print(charCount)
avgLineLen=(charCount/lineCount)
print("Line Count:",str(lineCount)+"\n"+"Character Count:",str(charCount))
print("Average Line Length:",str(avgLineLen))
