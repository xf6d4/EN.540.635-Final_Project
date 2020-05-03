'''
Created on May, 2
Classes that build a computer from components provided by ComponentClass
and check if components are applicable

@author LT_LUTUO
'''


class Computer(object):
    '''
    This is a class to build computers
    '''
    def __init__(self, name='MyComputer', cpu='', motherboard='', case='',
                 power_supply='', memory='', storage='', cooling='',
                 graphic='', os='', monitor='', mice='', keyboard=''):
        '''
        initiate the computer with its component

        **Parameters**
            cpu

            motherboard

            case

            power_supply

            memory

            storage

            cooling

            graphic

            os
        '''
        self.name = name
        self.cpu = cpu
        self.motherboard = motherboard
        self.case = case
        self.power_supply = power_supply
        self.memory = memory
        self.storage = storage
        self.cooling = cooling
        self.graphic = graphic
        self.os = os
        self.monitor = monitor
        self.mice = mice
        self.keyboard = keyboard
        self.component_type = list(self.__dict__.keys())
        self.component_type.pop(0)

    def __str__(self):
        msg = "\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s" \
            % (
                'Name', self.name,
                'CPU', self.cpu,
                'Motherboard', self.motherboard,
                'Memory', self.memory,
                'Storage', self.storage,
                'OS', self.os
                )
        return msg

    def __call__(self):
        return self.name

    def __repr__(self):
        msg = "\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s \
               \n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s\n\t%s:%s \
               \n\t%s:$%.2f\n\t%s:$%.2f" \
            % (
                'Name', self.name,
                'CPU', self.cpu,
                'Motherboard', self.motherboard,
                'Memory', self.memory,
                'Storage', self.storage,
                'Graphic', self.graphic,
                'OS', self.os,
                'Case', self.case,
                'Power', self.power_supply,
                'Cooling', self.cooling,
                'monitor', self.monitor,
                'mice', self.mice,
                'keyboard', self.keyboard,
                'Price', self.get_price(),
                'Shipping', self.total_shipping()
                )
        return msg

    def ifcompatible(self):
        if self.cpu.brand not in self.motherboard.detail:
            return False
        return True

    def get_price(self):
        price = 0
        for t in self.component_type:
            c = getattr(self, t)
            if type(c) != str:
                price += c.price
        return price

    def total_shipping(self):
        shipping = 0
        for t in self.component_type:
            c = getattr(self, t)
            if type(c) == str:
                pass
            elif c.shipping == 'Free Shipping':
                pass
            else:
                stop = c.shipping.index(' ')
                shipping += float(c.shipping[1:stop])
        return shipping
