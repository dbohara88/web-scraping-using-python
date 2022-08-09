import requests 
from bs4 import BeautifulSoup 
url = "https://en.wikipedia.org/wiki/India"
import csv

# Making a GET request
r = requests.get(url)

# Parsing the HTML
soup = BeautifulSoup(r.content,'html.parser')

# Removing all the tags
def remove_tags(html):
    for data in soup(['style'],['script']):
        data.decompose()
    
    return ' '.join(soup.stripped_strings)

print(remove_tags(r.content))

# Extracting all the links
for link in soup.find_all('a'):
    print(link.get('href'))

# Extracting Image Information
images_list = []
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src":src,"alt":alt})

for image in images_list:
    print(image)


# Writing to csv files
URL = 'https://www.geeksforgeeks.org/data-structures/?ref=shm'
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'html.parser')
 
titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []
 
count = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = title.text
    count += 1
    titles_list.append(d)
 
filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name'])
    w.writeheader()
     
    w.writerows(titles_list)



