# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:47:49 2020

@author: xf6d4
"""

import requests
from bs4 import BeautifulSoup
from csv import writer



url = ['https://www.newegg.com/CPUs-Processors/Category/ID-34?cm_sp=Tab_Components_1-VisNav-_-CPU-Processors_2',
       'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?cm_sp=Tab_Components_3-_-visnav-_-Video-Graphic-Devices_1',
       'https://www.newegg.com/Motherboards/Category/ID-20?cm_sp=Tab_Components_2-_-visnav-_-Motherboards_1',
       'https://www.newegg.com/Computer-Cases/Category/ID-9?cm_sp=Tab_Components_4-_-visnav-_-Computer-Cases_1',
       'https://www.newegg.com/Power-Supplies/Category/ID-32?cm_sp=Tab_Components_5-_-visnav-_-Power-Supplies_1',
       'https://www.newegg.com/Memory/Category/ID-17?cm_sp=Tab_Components_6-_-visnav-_-Memory_1',
       'https://www.newegg.com/Hard-Drives/Category/ID-15?cm_sp=Tab_Components_7-_-visnav-_-Storage_1',
       'https://www.newegg.com/Fans-Heatsinks/Category/ID-11?cm_sp=Tab_Components_9-_-visnav-_-Cooling_1']

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

    elif i == url[1]:
        Graphic_list = [Brand, Detail, Price, Link, Shipping]

    elif i == url[2]:
        Motherboard_list = [Brand, Detail, Price, Link, Shipping]

    elif i == url[3]:
        Case_list = [Brand, Detail, Price, Link, Shipping]

    elif i == url[4]:
        PowerSupply_list = [Brand, Detail, Price, Link, Shipping]

    elif i == url[5]:
        Memory_list = [Brand, Detail, Price, Link, Shipping]

    elif i == url[6]:
        Storage_list = [Brand, Detail, Price, Link, Shipping]

    elif i == url[7]:
        Cooling_list = [Brand, Detail, Price, Link, Shipping]

