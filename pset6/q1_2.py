with open("python_06.txt","r") as f_read, open("python_06_uc.txt","w") as f_write:
	for line in f_read:
		line=line.upper()
		f_write.write(line)
