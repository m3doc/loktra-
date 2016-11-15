import sys
import requests
import re
from BeautifulSoup import BeautifulSoup
args = sys.argv
keyword = args[1]



def getNumber(text):
    soup = BeautifulSoup(text)
    value= soup.findAll("span", {"class": "numTotalResults"})[0].string
    value = value.replace("&#43;","+")
    value = re.sub('.*of\s', '', value)
    return value


def getItems(text):
    soup = BeautifulSoup(text)
    value = soup.findAll("span", {"class": "quickLookGridItemFullName hide"})

    for item in value:
        item =item.string
        item = re.sub('<.*>','',item)
        item = re.sub('</span>','',item)
        print item

    # print len(value)
if len(args)==2:
    data = requests.get('http://www.shopping.com/products?KW=' + keyword)
    print getNumber(data.text)
elif len(args)==3:
    pageNumber = args[2]

    data = requests.get('http://www.shopping.com/products~PG-'+pageNumber+'?KW='+keyword)
    #print data.text
    getItems(data.text)

















