import requests 
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
html = response.text
links = []
soap = BeautifulSoup(html,'html.parser')
pages = soap.find_all(class_='page')
#print(pages)
for page in pages:
	if page.find('a') != None:
		#print(page.find('a').attrs['href'])
		links.append(page.find('a').attrs['href'])
#print(links)
print(links[0])
for i in range(len(links)):
	response = requests.get("https://www.rithmschool.com"+links[i])
	print("https://www.rithmschool.com"+links[i])

articles = soap.find_all("article")
with open ("website.csv", 'w') as cv_file, open("website1234.csv",'w') as cv_file1234:
	for i in range(len(links)):
		if i == 0:
			print('here')
			response = requests.get("https://www.rithmschool.com/blog")
			html = response.text
			soap = BeautifulSoup(html,'html.parser')
			articles = soap.find_all("article")
			#pages = soap.find_all(class_='page')
			csv_writer = writer(cv_file)
			csv_writer.writerow(['title', 'link', 'date'])
			for article in articles:
				text = article.find('a').get_text()
				tags = article.find('a').attrs['href']
				date = article.find('time')['datetime']
				csv_writer.writerow([text, tags, date])
		if i > 0:
			print('here1')
			response = requests.get("https://www.rithmschool.com"+links[i])
			html1 = response.text
			soap = BeautifulSoup(html1,'html.parser')
			#pages = soap.find_all(class_='page')
			articles = soap.find_all("article")
			csv_writer1 = writer(cv_file1234)
			csv_writer1.writerow(['title', 'link', 'date'])
			for article in articles:
				text = article.find('a').get_text()
				tags = article.find('a').attrs['href']
				date = article.find('time')['datetime']
				csv_writer1.writerow([text, tags, date])