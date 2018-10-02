import requests

url="https://www.brainyquote.com/topics/age"

page = requests.get(url)

# print(page.text)

from bs4 import BeautifulSoup

soup=BeautifulSoup(page.text, 'html.parser')

quotes=soup.find_all('a', class_='b-qt') #find an anker tag with the class b-qt

print(quotes)

for item in quotes:
    print(item.contents[0].strip())