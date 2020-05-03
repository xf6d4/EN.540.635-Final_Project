# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:47:49 2020

@author: xf6d4
"""

import requests
from bs4 import BeautifulSoup
from csv import writer
from ComponentClass import Component


def scraper(url):
    component_type = [*url]
    component_list = {t + '_list': [] for t in component_type}

    for t in component_type:
        i = url[t]
        response = requests.get(i)
        # Get webpage text
        webpage = BeautifulSoup(response.text, 'html.parser')
        # Find out each item listed in the webpage
        items = webpage.findAll('div', {'class': 'item-container'})
        for item in items:
            # Scrap brand
            brand = item.find(class_='item-branding').a.img["title"]
            # Scrap details
            detail = item.a.img["title"]
            # Scrap price
            price = item.find(class_='price-current').get_text()
            toremove = dict.fromkeys((ord(c) for c in u'\xa0\n\t, $-'))
            price = price.translate(toremove)
            stop = price.index('.') + 3
            price = price[:stop]
            # Scrap web link
            link = item.a["href"]
            # Scrap shipping info
            shipping = item.find(class_='price-ship').get_text().strip()
            c = Component(t, brand, detail, price, link, shipping)
            component_list[t + '_list'].append(c)
        if component_list[t + '_list'] == []:
            raise AssertionError('No items are found with the link for %s' % t)
        print('Scraping for %s is success' % t)
    return component_list
