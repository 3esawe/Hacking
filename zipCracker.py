import zipfile 

def guess(zifle,pwd):
	zip = zipfile.ZipFile('omar.zip')
	try: 
		zip.exctractall(pwd)
		return pwd
	except:
		return



def main():
	zip = zipfile.ZipFile('omar.zip')
	with open('words2') as file:
		for word in file: 
			l = word.strip("\n")
			x = guess(zip,l)
			if x:
				print(x)
				exit(0)





if __name__ == '__main__':
	main()