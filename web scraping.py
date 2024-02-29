import requests 
from bs4 import BeautifulSoup 
  
  
# Making a GET request 
r = requests.get('https://www.tensorflow.org/api_docs/python/tf') 
  
# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 
  
s = soup.find('section') 
content = s.find_all('a') 
for line in content:
    print(line.text,end='\n')
