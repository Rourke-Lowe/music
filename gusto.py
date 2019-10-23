# going through multiple pages on discogs

import requests
from bs4 import BeautifulSoup
import re
import csv

releases = []
pages = []


for i in range(1,22):
    website_url = requests.get('https://gusto.com/partners/directory/results?company_sizes_served%5B%5D=&industries_served%5B%5D=E-commerce&location=&page=' + format(i))
    pages.append(website_url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'lxml')


    file = csv.writer(open('gustoscrape.csv', 'w'))
    file.writerow(['company','website','email','phone','location','desc'])

    rows = find_all('div', class = 'card-hover bg-white box-shadow border-radius-5px')

    for row in rows:
        compdata = {}
        company = row.find('div', class ='h6-centra margin-bottom-10px padding-top10px padding-right-25px' )
        website = row.find('a', class = 'c-black-1000 text-decoration-none js-website')
        email = row.find('a', class = 'c-black-1000 text-decoration-none js-email')
        phone = row.find('a', class = 'c-black-1000 text-decoration-none')
        location = row.find('span', class = 'c-black-800')
        desc = row.find('div', class = 'd-none d-lg-block col-12 word-wrap-break')


        compdata['company'] = company.text
        compdata['website'] = website.find('a')['href']
        compdata['email'] = email.find('a')['href']
        compdata['phone'] = phone.text
        compdata['location'] = location.text
        compdata['desc'] = desc.text

        file.writerow([compdata])
