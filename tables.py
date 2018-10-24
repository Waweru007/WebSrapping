import urllib
import urllib.request
from bs4 import BeautifulSoup

def make_soup(url):
    thepage=urllib.request.urlopen(url)
    soupdata=BeautifulSoup(thepage, "html.parser")
    return soupdata
soup=make_soup("https://data.lacounty.gov/Parcel-/Assessor-Parcels-Data-2018/mk7y-hq5p")

for record in soup.findAll("outerContainer"):
    for data in record.findAll("tr"):
        print(data.text)
