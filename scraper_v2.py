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
    '''
    This function scrap product info from www.newegg.com
    and initiate theminto components of the computer
    with a give dict of urls

    **Parameter**
        url:*dict,str*
            A dict that contain info for component names and its url.
            Keys should be component names that are in README or ComputerClass
            Hashes should be its product url from www.newegg.com

    **Output**
        component_list:*dict,str:object*
            A dict that contain info for lists of components
            Keys are name of the components with _list
            Hashes are objects after initiating with component class

    **Error**
        KeyError:*str*
            Error if keys' name in url do match possible ones in ComputerClass
        AssertionError:*str*
            Error if links in hashes are not str
        LinkError:*str*
            Error if links are not from www.newegg.com
        AttributeError:*str*
            Error if no products are found in the web link
    '''
    component_type = list(url.keys())
    component_list = {t + '_list': [] for t in component_type}

    pos_component = [
        'cpu', 'motherboard', 'case', 'power_supply', 'memory', 'storage',
        'cooling', 'graphic', 'os', 'monitor', 'mice', 'keyboard', 'test'
    ]
    assert all(t in pos_component for t in component_type), \
        'KeyError: Please refer to readme for possible component names '\
        'and change the name in keys for url'

    for t in component_type:
        i = url[t]
        assert isinstance(i, str), 'please input links for %s as str' % t
        assert 'www.newegg.com' in i, \
            'LinkError: This scraper only works for links for www.newegg.com'
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
            raise AttributeError('No items are found with the link for %s' % t)
        print('Scraping for %s is success' % t)
    return component_list
