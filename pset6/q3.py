with open("python_06.seq.txt","r") as f_read,open("python_06.revComp.txt","w") as f_write:
	compDict={'T':'A','A':'T','C':'G','G':'C','N':'N'}
	for line in f_read:
		seqID,seq=line.split()
		#print(seq)
		compSeq=''
		for letter in seq:
			#print(letter)
			compLetter=compDict[letter]
			#print(compLetter)
			compSeq+=compLetter
	#		print(compSeq)
		
			print(compSeq[::-1])
	
