

from bs4 import BeautifulSoup
import requests
import csv

url = 'https://old.reddit.com/r/tennis/'
headers = {'user-agent': 'Chrome/73.0.3683.86'}

csv_file = open('redditscrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'Link', 'likes'])
loop=0
while(loop<100):


	page = requests.get(url,headers=headers)

	soup = BeautifulSoup(page.text, 'lxml')


	
	x=[]
	therafa=[]
	


	count=0
	for i in soup.find_all("div", attrs={'class':'thing'}):
		if count==0 or count==1:
			count=count+1
			continue

		
		#print(link['href'])
		

		#print(likes)
		title=i.find("p",class_="title").text
		if 'Rafa' in title:
			therafa.append(title)
			print(title)
		elif 'rafa' in title:
			therafa.append(title)
			print(title)
		elif 'nadal' in title:
			therafa.append(title)
			print(title)
		elif 'Nadal' in title:
			therafa.append(title)
			print(title)
		else:
			 #therafa.append(title)
			#print(title,'NO')
			continue

		link=i.find('a')['href']
		link2="https://www.reddit.com"
		if(link.startswith('https')!=True):
			link = link2+link
		print(link)
		likes = i.find("div", attrs={"class": "score likes"}).text

		csv_writer.writerow([title,link,likes])


	#hehe=soup.select('div>span.nextbutton')
	x = soup.select("div>span>span.next-button")
	for _ in x:
		z=_
		url = z.find('a')['href']



	loop=loop+1

	print('\n\n\n\n')
	print(len(therafa))






csv_file.close()
