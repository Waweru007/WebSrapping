import requests

url="https://www.scoopwhoop.com/inothernews/richest-criminals/#.emeo66mu3"

page = requests.get(url)

# print(page.text)

from bs4 import BeautifulSoup

soup=BeautifulSoup(page.text, 'html.parser')

quotes=soup.find_all(class_="quoteText")

# print(quotes)
file=open("Quotes.txt", "w+")  #Open a new text file

for item in quotes:
    data=item.contents[0]
    data=data.strip()   #Remove spaces
    data = data.replace('“', '')    #Remove quotes
    data = data.replace('”', '')  #replace quotes with nothing
    print(data)
    file.write(data+"\n")    #Save he data

