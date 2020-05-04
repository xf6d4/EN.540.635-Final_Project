'''
Created on May, 2
Classes that store the information of components

@author: LT_LUTUO
@coauthor: xf6d4
'''


class Component(object):
    '''
    this is the class for components in a computer
    it store all the informations of the component including type, brand,
    detail, price, link and shipping
    '''
    def __init__(self, type=None, brand=None, detail=None, price=None, 
                 link=None, shipping=None):
        '''
        initiate the component with its informations

        **Parameters**
            brand:*str*
                The brand of the component
            detail:*str*
                The detail info of the component
            price:*str*
                The price of the component
            link:*str*
                The web link for the component
            shipping:*str*
                The shipping cost for the component

        **Output**
            None

        **Error**
            None
        '''
        self.type = type
        self.brand = brand
        self.detail = detail
        self.price = price
        self.link = link
        self.shipping = shipping

    def __str__(self):
        '''
        '''
        return self.detail

    def __call__(self):
        '''
        '''
        return self.type

    def __repr__(self):
        '''
        '''
        msg = "\n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s" \
            % (
                'Brand', self.brand,
                'Detail', self.detail,
                'Price', self.price,
                'Link', self.link,
                'Shipping', self.shipping
                )
        return msg
