
from bs4 import BeautifulSoup
import requests
import csv


headers = {'user-agent': 'Chrome/73.0.3683.86'}

csv_file = open('google.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'Link',])
loop=0
print("Enter your search query:")
query=input()
print("\n","Enter the number of pages you wanna search through")
loop=int(input())
url ="https://www.google.com/search?q="+query


pager=2
while(loop!=0):


	page = requests.get(url,headers=headers)

	soup = BeautifulSoup(page.text, 'lxml')
	"""
	for i in soup.find_all("td",class_="b"):
		for j in i.find_all('a'):
			x=str(j)
			ffs=x.split(' ')
			link=ffs[2]
			list2=link.split('"')
			print(list2[1])


	"""
	counter=0

	for i in soup.select("div.g"):

		if counter==9:
			break


		elif(counter>=1):	
			z=i.find('a')
			title=z.text
			link=z['href']
			link=link[7:]
			print(title,"got one","\n\n")
			csv_writer.writerow([title,link])
		counter=counter+1
		
	pager=pager+1	

	url="http://www.google.com/search?q=" + query + "&start=" + str((pager - 1) * 10)
	loop=loop-1






csv_file.close()
