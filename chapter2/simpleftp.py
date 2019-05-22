import ftplib 


def connect(host): 
	try:
		ftp = ftplib.FTP(host)
		ftp.login()
		ftp.retrlines("LIST")
		return True
	except:
		print("Failed")
		return False
connect('ftp.debian.org')