from scapy.all import * 

def ddosTest(src, dest, iface, count):
	pkt = IP(src=src, dst=dest) / ICMP(type=8, id = 678) / Raw(load='1234')
	send(pkt,iface=iface ,count = count)
	pkt = IP(src=src, dst=dest) / ICMP(type=0) / Raw(load='AAAAAAAAAA')
	send(pkt,iface=iface ,count = count)
	pkt = IP(src=src, dst=dest) / UDP(dport=31335) / Raw(load='PONG')
	send(pkt,iface=iface ,count = count)
	pkt = IP(src=src, dst=dest) / ICMP(type=0,  id = 456)
	send(pkt,iface=iface ,count = count)
src= '10.0.2.15'
dest = '10.0.2.8'
count =1 
iface = 'enp0s3'
ddosTest(src,dest,iface,count)