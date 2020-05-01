# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:47:49 2020

@author: xf6d4
"""

import requests
from bs4 import BeautifulSoup
from csv import writer


#def CPU():
#
#    response = requests.get('https://www.newegg.com/CPUs-Processors/Category/ID-34?cm_sp=Tab_Components_1-VisNav-_-CPU-Processors_2')
#    # Get webpage text
#    webpage = BeautifulSoup(response.text, 'html.parser')
#    # Find out each item listed in the webpage
#    items = webpage.findAll("div", {"class": 'item-container'})
#
#    Brand = []
#    Detail = []
#    Price = []
#    Link = []
#    Shipping = []
#    for item in items:
#        # Scrap brand
#        brand = item.find(class_='item-branding').a.img["title"]
#        # Scrap details
#        detail = item.a.img["title"]
#        # Scrap price
#        price = item.find(class_='price-current').get_text()
#        toremove = dict.fromkeys((ord(c) for c in u'\xa0\n\t '))
#        price = price.translate(toremove)
#        # Scrap web link
#        link = item.a["href"]
#        # Scrap shipping info
#        shipping = item.find(class_='price-ship').get_text().strip()
#        Brand.append(brand)
#        Detail.append(detail)
#        Price.append(price)
#        Link.append(link)
#        Shipping.append(shipping)
#
#    CPU_list = [Brand, Detail, Price, Link, Shipping]
#    print(CPU_list)



url = ['https://www.newegg.com/CPUs-Processors/Category/ID-34?cm_sp=Tab_Components_1-VisNav-_-CPU-Processors_2',
       'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?cm_sp=Tab_Components_3-_-visnav-_-Video-Graphic-Devices_1']
for i in url:
    
    response = requests.get(i)
    # Get webpage text
    webpage = BeautifulSoup(response.text, 'html.parser')
    # Find out each item listed in the webpage
    items = webpage.findAll("div", {"class": 'item-container'})

    Brand = []
    Detail = []
    Price = []
    Link = []
    Shipping = []
    for item in items:
        # Scrap brand
        brand = item.find(class_='item-branding').a.img["title"]
        # Scrap details
        detail = item.a.img["title"]
        # Scrap price
        price = item.find(class_='price-current').get_text()
        toremove = dict.fromkeys((ord(c) for c in u'\xa0\n\t '))
        price = price.translate(toremove)
        # Scrap web link
        link = item.a["href"]
        # Scrap shipping info
        shipping = item.find(class_='price-ship').get_text().strip()
        Brand.append(brand)
        Detail.append(detail)
        Price.append(price)
        Link.append(link)
        Shipping.append(shipping)
    if i == url[0]:
        CPU_list = [Brand, Detail, Price, Link, Shipping]
        print(CPU_list)
    elif i == url[1]:
        Graphic_list = [Brand, Detail, Price, Link, Shipping]
        print(Graphic_list)




#item = items[5]
#price = item.find(class_='price-current').get_text()
#toremove = dict.fromkeys((ord(c) for c in u'\xa0\n\t '))
#price = price.translate(toremove)
