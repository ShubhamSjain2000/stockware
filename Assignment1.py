import random
import requests 
from bs4 import BeautifulSoup 
import csv 
lst =[]
lst2=[]
URL = "https://money.rediff.com/index.html"
    #URL = "https://money.rediff.com/indices/nse"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html.parser') 
anchors = soup.find_all('td',class_='numericalColumn')

print(anchors)
for anchor in anchors:
        lst.append(anchor.get_text())
	    #print(anchor)
print("list11 us ",lst)
for x in lst[0:2]:
        z = x[-6:-1]
        y = x[0:2]
        
        
        lst2.append(y+z)
print(lst2)
#print(soup.find_all('span',class_='red'))
#print(soup.find('p').get_text())
#print(soup.get_text())
   