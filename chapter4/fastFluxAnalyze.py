from scapy.all import * 

dnsRecord = {}

def handlePkt(pkt):
	if pkt.haslayer(DNSRR): 
		rrname = pkt.getlayer(DNSRR).rrname
		rdata = pkt.getlayer(DNSRR).rdata
		if dnsRecord.has_key(rrname):
			if rdata not in  dnsRecord[rrname]:
				dnsRecord[rrname].append(rdata)
		else :
			dnsRecord[rrname] = []
			dnsRecord[rrname].append(rdata)
def main():
	pkts = rdpcap('fastFlux.pcap')
	for pkt in pkts:
		handlePkt(pkt)
	for item in dnsRecord:
		print '[+] ' + item + ' has ' + str(len(dnsRecord[item])) + ' unique IP'

if __name__ == '__main__':
	main()