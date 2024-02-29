# This is the first piece of program from our project we have been researching about different websites to get the most effective dataset to include in our project
import requests 
from bs4 import BeautifulSoup 
r = requests.get('https://www.tensorflow.org/api_docs/python/tf') 
soup = BeautifulSoup(r.content, 'html.parser') 
s = soup.find('section') 
content = s.find_all('a') 
for line in content:
    print(line.text,end='\n')
