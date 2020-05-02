'''
Created on May, 2
Classes that store the information of components

@author LT_LUTUO
'''


class Component(object):
    '''
    this is the class for components in a computer
    '''
    def __init__(self, type, brand, detail, price, link, shipping):
        '''
        initiate the component with its informations

        **Parameters**
            brand:

            detail:

            price:

            link:

            shipping:

        '''
        self.type = type
        self.brand = brand
        self.detail = detail
        self.price = price
        self.link = link
        self.shipping = shipping

    def __str__(self):
        return self.detail

    def __call__(self):
        return self.type

    def __repr__(self):
        msg = "\n%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s" \
            % (
                self.type, self.brand,
                'Detail', self.detail,
                'Price', self.price,
                'Link', self.link,
                'Shipping', self.shipping
                )
        return msg
