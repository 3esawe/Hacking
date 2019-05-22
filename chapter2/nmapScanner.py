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


def connectToHost(targethost, targetport):
	nm = nmap.PortScanner() 
	nm.scan(targethost,targetport)
	state = nm[targethost]['tcp'][int(targetport)]['state']
	print(state)
	print ('targethost: ' + targethost + ' targetport: ' + targetport)

def main():
	targethost, targetports = parsing()
	for i in targetports:
		connectToHost(targethost,i)

if __name__ == '__main__':
	main()