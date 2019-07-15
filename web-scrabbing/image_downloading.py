import requests 
from bs4 import BeautifulSoup
import os 
import shutil

if os.path.isdir('images'):
	shutil.rmtree('images')

else:
	os.makedirs('images')

web_page = requests.get('https://en.wikipedia.org/wiki/Dennis_Ritchie')
html = web_page.text
soap = BeautifulSoup(html, 'lxml')

for img in soap.find_all('img'):
	print ("Downloading this image: "  + img['src'])
	res = requests.get("https:"+img['src'])
	image = open(os.path.join('images', os.path.basename(img['src'])), 'wb')
	for chunck in res.iter_content(1000):
		image.write(chunck)	
	image.close()
