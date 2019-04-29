

import urllib.request as urllib2
#z=str(input()) # give input url
z ="https://imgur.com/search/score?q="
print("input search query for imgur")
k=str(input())

z=z+k

source = urllib2.urlopen(z)

from bs4 import BeautifulSoup

soup = BeautifulSoup(source.read(),features='lxml')
num=1
counter=5
print("enter the number of pics you want")
counter=int(input())
for i in soup.find_all('img'):
	link=i.get('src')
	print(z+link)
	link="https:"+link
	
	data= urllib2.urlopen(link).read()
	num=num+1
	x=str(num)
	x=x+'.jpeg'
	with open(x,'wb') as stream:
		stream.write(data)
	counter-=1
	if counter==0:
		break	
