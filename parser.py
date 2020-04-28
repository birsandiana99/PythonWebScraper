#import requests and beautifulSoup
import requests
from bs4 import BeautifulSoup
#library for regular expressions
import re

link = 'http://traxdb.blogspot.com/'

raw_html = requests.get(link)

# print(raw_html.text)

# builds the BeautifulSoup variable
soup = BeautifulSoup(raw_html.text, 'html.parser')
# print(soup)

# results = soup.find_all('a')
# print(results)


# open the link file in append mode
file = open('input.txt', 'r')
# read from file to make sure we don't write any duplicates
file_content = []
lines = file.readlines()

for line in lines:
    file_content.append(line)

# print(file_content)

file.close()

file = open('input.txt', 'w')

# digest the links and write them to the file
for raw_link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
    if raw_link.get('href').endswith("file.html"):
        link = raw_link.get('href')
        link = link[0: 4:] + link[5::]
        if link not in file_content:
            print(link)
            file.write(link)
            file.write("\n")

file.close()

