import zipfile 
from threading import Thread 
import optparse 
def guess(zifle,pwd):
	zip = zipfile.ZipFile('omar.zip')
	try: 
		zip.exctractall(pwd)
		print ("found pass "+ pwd)
	except:
		return


def main():
	parser = optparse.OptionParser("usage%prog"+ 
		"-f <zip file> -d <dir>")
	parser.add_option('-f', dest='zname', type='string', help='specify zip name')
	parser.add_option('-d', dest='dname', type='string', help='specify file name')
	(options, args) = parser.parse_args()
	if (options.zname == None or (options.dname == None)):
		exit(0)
	else:
		zname = options.zname
		dname = options.dname 
	zip = zipfile.ZipFile(zname)
	with open(dname) as file:
		for word in file: 
			l = word.strip("\n")
			t = Thread(target=guess, args =(zip,l)) # the function name is the target and args are it's argument
			t.start()



if __name__ == '__main__':
	main()