import bs4
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.ycombinator.com/topcompanies/').text

soup= BeautifulSoup(source,'lxml')

csv_file= open('csmwrite.csv','w')
csv_writer =csv.writer(csv_file)

csv_writer.writerow(['Name','Hyper','Description','Founders','Sector','Jobs created'])
#csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)


Hyper=''
Founders=[]
soup.prettify()
z=''
z2=[]
count=0
lister=[z,"","","","","","",""]
ff=""
na=""
d=""
j=""
s=""




for tablerows in soup.find_all('tr'):
	
	#Hyperlinks

	for i in tablerows.find_all('td'):
		count=0
		for l in i.find_all('a'):
			z=l['href']
			count=count+1;

		#print(count)
		if(count==1):
			print(z)
   ######################################
   #NAME
	xd = tablerows.select("td:nth-of-type(1) b.h4 ")
	for _ in xd:
		print(_.text)
		na=str(_.text)
	
	#####################################
	#LINKS
	link = tablerows.select("td:nth-of-type(1) a")
	for i in link:
		Hyper=i['href']



	
	



   ######################################
   #Description

	v=tablerows.select('td:nth-of-type(3)')
	for _ in v:
		print(_.text)
		d=str(_.text)

	print('\t')
	#csv_writer.writerow(["","","",z,"","","",""])
	#####################################
	jobs=tablerows.select('td:nth-of-type(6) span')
	for _ in jobs:
		print(_.text)
		j=_.text


	#####################################
	#Sectors
	sectors=tablerows.select("td:nth-of-type(5) p")
	for _ in sectors:
		print(_.text)
		s=_.text

    ######################################
    #Founders

	for z2 in tablerows.find_all('td',class_='founders'):
	#print(z2.contents)
	#print(z2.contents[1].contents)
		ff=[]
		hello=z2.contents[1].contents
		while ' ' in hello:
			hello.remove(' ')

		for i in hello:
			print(i.text)
			ff.append(i.text)



	#csv_writer.writerow([na,Hyper,d,ff,s,j])
			#ff.append(i.text)

		ff='   '.join(ff)
		csv_writer.writerow([na,Hyper,d,ff,s,j])

	

	print("\n")

	print(Hyper)
	
	#####################################

print('Wot')