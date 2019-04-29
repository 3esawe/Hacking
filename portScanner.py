import nmap
import optparse
from socket import *

def parsing():
	parser = optparse.OptionParser("usage -H for target host \n" + "usage -P for target port");
	parser.add_option('-H', dest='targethost',type='string')
	parser.add_option('-P', dest='targetport', type='string')

	(options, args) = parser.parse_args()
	targetport = str(options.targetport).split(',')
	targethost = options.targethost
	if targethost == None or targetport == None:
		exit(0)
	return (targethost, targetport)

def connScan(host , port):
	try:
		sockfd = socket(AF_INET, SOCK_STREAM)
		sockfd.connect((host, port))
		sockfd.send("Hello")
		res = sockfd.recv(1024)
		print ("opend tcp connection with ", port, res)
		sockfd.close()
	except:
		print ("error has occcured in tcp connection")


def portScan(host, ports):
	try:
		trgIP = gethostbyname(host)
	except:
		print ("cannot resolve that ip address for this host")
		return 
	try:
		trgName = gethostbyaddr(trgIP)
		print ("Scan result for: " ,trgName[0])
	except:
		print ("Scan result for: " ,trgIP)
	
	for port in ports:
		connScan(trgIP,int(port))


def main():
	targethost, targetport = parsing()
	print(targethost)
	print(targetport)
	portScan(targethost, targetport)

if __name__ == '__main__':
	main()
