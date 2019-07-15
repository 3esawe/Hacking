from scapy.all import *


def dnsQRTest(pkt):
	if pkt.haslayer(DNSRR) and pkt.getlayer(UDP).sport == 53:
		rcode = pkt.getlayer(DNS).rcode
		qname = pkt.getlayer(DNSQR).qname
		if rcode == 3:
			print '[-] lookup failed' + qname
			return True
		else : return False  



def main():
	notAnswerd = 0
	pkts = rdpcap("domainFlux.pcap")
	type(pkts)
	for pkt in pkts:
		if dnsQRTest(pkt):
			notAnswerd += 1
	print 'total unanwered is: ' + str(notAnswerd)


if __name__ == '__main__':
	main()