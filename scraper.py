# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:35:09 2020

@author: xf6d4
"""

import requests
from bs4 import BeautifulSoup
from csv import writer

#
response = requests.get('https://www.newegg.com/Gaming-Desktops/Store/ID-2125620?name=Gaming-Desktops')

# Get webpage text
webpage = BeautifulSoup(response.text, 'html.parser')

# Find out each item listed in the webpage
items = webpage.findAll("div", {"class": 'item-container'})

with open('Computer.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Brand', 'Details', 'Shipping']
    csv_writer.writerow(headers)

    for item in items:
        brand = item.find(class_='item-branding').a.img["title"]
        detail = item.a.img["title"]
        #price = item.find(class_='price-current').get_text()
        shipping = item.find(class_='price-ship').get_text().strip()
        
        csv_writer.writerow([brand, detail, shipping])



#computer = pd.DataFrame(
#        {'Brand': brand, 
#         'Details': detail,
#         'Shipping': shipping,
#         })
#    

# References:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/