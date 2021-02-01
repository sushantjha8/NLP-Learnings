


from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.drugs.com/search.php?searchterm=Jardiance&a=1').text

soup = BeautifulSoup(source, 'lxml')


with open('crawl.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

filename = "crawl.csv"
fields = ['name', 'information', 'prescription']
#csvwriter.writerow(fields)

with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields)
    name = soup.find('div', class_= 'ddc-media-content ddc-search-result ddc-search-result-with-secondary')
    named = name.a.h3.text
    print(named)
    print()
    print('****')
    print()

    information = soup.find('div', class_= 'ddc-media-content ddc-search-result ddc-search-result-with-secondary').a.p.text
    print(information)
    print()
    print('****')
    print()
    prescribe_info = soup.find('div', class_= 'ddc-media-content ddc-search-result').a.p.text
    print(prescribe_info)

    records = [named,information,prescribe_info]
    csvwriter.writerow(records)

csvfile.close()