# This is the first piece of program from our project we have been researching about different websites to get the most effective dataset to include in our project
import requests 
from bs4 import BeautifulSoup 
r = requests.get('https://www.tensorflow.org/api_docs/python/tf') 
soup = BeautifulSoup(r.content, 'html.parser') 
s = soup.find('section') 
content = s.find_all('a') 
for line in content:
    print(line.text,end='\n')

import requests 
from bs4 import BeautifulSoup 
r = requests.get('https://www.tensorflow.org/api_docs/python/tf') 
soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.title) 
print(soup.title.name) 
print(soup.title.parent.name) 
import requests 
from bs4 import BeautifulSoup 


# Making a GET request 
r = requests.get('https://www.tensorflow.org/api_docs/python/tf') 

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

s = soup.find('div', class_='entry-content') 
content = s.find_all('p') 

print(content)
import requests 
from bs4 import BeautifulSoup 


# Making a GET request 
r = requests.get('https://www.tensorflow.org/api_docs/python/tf') 

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

# Finding by id 
s = soup.find('div', id= 'main') 

# Getting the leftbar 
leftbar = s.find('ul', class_='leftBarList') 

# All the li under the above ul 
content = leftbar.find_all('li') 

print(content)

import requests 
from bs4 import BeautifulSoup 


# Making a GET request 
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

s = soup.find('div', class_='entry-content') 

lines = s.find_all('p') 

for line in lines: 
	print(line.text)
import requests 
from bs4 import BeautifulSoup 


# Making a GET request 
r = requests.get('https://www.python.org/') 

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

# Finding by id 
s = soup.find('div', id= 'main') 

# Getting the leftbar 
leftbar = s.find('ul', class_='leftBarList') 

# All the li under the above ul 
lines = leftbar.find_all('li') 

for line in lines: 
	print(line.text)

