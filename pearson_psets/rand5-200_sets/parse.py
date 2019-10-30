import re
with open("cat_file.txt","r")as f:
	for line in f:
		line=line.rstrip()
		if "ssearch36" in line:
			line=line.split()
			scoreMatrix=line[5]
			#print(scoreMatrix)
			continue
		if line.startswith("random"):
			splitLine=line.split()
			query=splitLine[0]
			subID=splitLine[1]
			pcID=splitLine[2]
			alignLen=splitLine[3]
			mismatch=splitLine[4]
			gap=splitLine[5]
			qStart=splitLine[6]
			qEnd=splitLine[7]
			sStart=splitLine[8]
			sEnd=splitLine[9]
			eVal=splitLine[10]
			bScore=splitLine[11
]
			line.replace(query,scoreMatrix)
			print("Score Matrix:"+scoreMatrix,"%ID"+pcID,"Alignment Length:"+alignLen,"E-value:"+eVal)

