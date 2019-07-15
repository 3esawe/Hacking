import dpkt
import socket


def printPcap(pcap):
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dest = socket.inet_ntoa(ip.dst)
			print ("Src--->{0} Dest--->{1}".format(src, dest))
		except Exception as e:
			print e 


if __name__ == '__main__':
	f = open('2019-06-22-traffic-analysis-exercise.pcap')
	pcap = dpkt.pcap.Reader(f)
	printPcap(pcap)