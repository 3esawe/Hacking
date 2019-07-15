from scapy.all import * 
from IPy import IP  as IPTEST
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		ttl = 5
		ttlDict = {}
		THRESH = 5


				
	def checkTLL(self, ipsrc, ttl):
	    if IPTEST(ipsrc).iptype() == 'PRIVATE':
	        return

	    if not ttlDict.has_key(ipsrc):
	        pkt = sr1(IP(dst=ipsrc) / ICMP(), \
	          retry=0, timeout=1, verbose=0)
	        ttlDict[ipsrc] = pkt.ttl

	    if abs(int(ttl) - int(ttlDict[ipsrc])) > THRESH:
	        print '\n[!] Detected Possible Spoofed Packet From: '\
	          + ipsrc
	        print '[!] TTL: ' + ttl + ', Actual TTL: ' \
	            + str(ttlDict[ipsrc])


	def testTLL(self, pkt):
		try:
			if pkt.haslayer(IP):
				ipsrc = pkt.getlayer(IP).src
				ttl = str(pkt.ttl)
				print ("[+] receiverd from: " + ipsrc + " with ttl: " + ttl)
		except Exception as e: 
			print(e)


if __name__ == '__main__':
	sniff(prn=testTLL, store=0)