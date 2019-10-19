with open("alpaca_all_genes.tsv","r") as alpacaAll, open("alpaca_pigmentation_genestxt.txt","r") as pig, open("alpaca_stemcellproliferation_genes.txt","r") as SC :
	alpacaGeneID=set()
	alpacaPig=set()
	alpacaSC=set()
	SCandPig=set()
	notProlif=set()
	for line in alpacaAll:
		line=line.split("\t")
		geneID=line[0]
		alpacaGeneID.add(geneID)
	for line in pig:
		line=line.split("\t")
		geneID=line[0]
		alpacaPig.add(geneID)
	for line in SC:
		line=line.split("\t")
		geneID=line[0]
		alpacaSC.add(geneID)

	###below code to find all genes that are not proliferation genes
	for i in alpacaPig:
		notProlif.add(i)
	for i in alpacaGeneID:
		notProlif.add(i)
	#print(notProlif)
	print(len(notProlif))
	###below code to find all genes that are both stem cell proliferation genes and pigment genes
	for i in alpacaSC:
		if i in alpacaPig:
			SCandPig.add(i)
	for i in alpacaPig:
		if i in alpacaSC:
			SCandPig.add(i)

	#print(SCandPig)
