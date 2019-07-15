import nmap 


def findTarget(subnet):
	nScan = nmap.PortScanner()
	nScan.scan(subnet, 445)
	openPorts = []
	for i in nScan.all_hosts():
		if nScan[i].has_tcp(445):
			state = nScan[i]['tcp'][445]['state']
			if state == 'open':
				openPorts.append(i)
				print('found host: ' , i)
	return openPorts


