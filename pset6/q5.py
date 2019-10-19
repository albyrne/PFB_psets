with open("python_06.fastq","r")as f_read:
	fastaDict={}
	lineCount=0
	for line in f_read:
		line=line.strip()
		lineCount+=1
		if lineCount%4==1:
			seqID=line
		#	print(seqID)
		elif lineCount%4==2:
			seq=line
			tab_delim_fasta=seqID+"\t"+seq
			fastaDict[seqID]=seq
	print(fastaDict)	
