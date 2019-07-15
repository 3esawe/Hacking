import csv


with open ('GeoLite2-City-Blocks-IPv4.csv', 'r') as handler: 
	reader = csv.DictReader(handler)
	for i in reader:
		if i['network'] == '1.0.1.0/24':
			print(i)