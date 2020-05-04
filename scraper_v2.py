# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:47:49 2020

@author: xf6d4
@coauthor: LT_LUTUO
"""

import requests
from bs4 import BeautifulSoup
from ComponentClass import Component


def scraper(url):
    component_type = list(url.keys())
    component_list = {t + '_list': [] for t in component_type}
    pos_component = [
        'cpu', 'motherboard', 'case', 'power_supply', 'memory', 'storage',
        'cooling', 'graphic', 'os', 'monitor', 'mice', 'keyboard', 'test'
    ]
    # for t in component_type:
    #     if t not in pos_component:
    #         raise AssertionError('Please refer to readme for possible \
    #              component names and change your name in keys for url')
    assert all(t in pos_component for t in component_type), \
        'Please refer to readme for possible component names '\
        'and change the name in keys for url'

    for t in component_type:
        i = url[t]
        assert isinstance(i, str), 'please input links for %s as str' % t
        assert 'www.newegg.com' in i, \
            'This scraper only works for links for www.newegg.com'
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
            try:
                float(price)
            except ValueError:
                price = 'Unknown'
            # Scrap web link
            link = item.a["href"]
            # Scrap shipping info
            shipping = item.find(class_='price-ship').get_text().strip()
            if shipping == 'Free Shipping':
                shipping = 0
            elif isinstance(shipping, (float, int)):
                pass
            elif shipping is str:
                stop = c.shipping.index(' ')
                shipping = c.shipping[1:stop]
                try:
                    float(shipping)
                except ValueError:
                    shipping = 'Unknown'
            c = Component(t, brand, detail, price, link, shipping)
            component_list[t + '_list'].append(c)
        if component_list[t + '_list'] == []:
            raise AssertionError('No items are found with the link for %s' % t)
        print('Scraping for %s is success' % t)
    return component_list
