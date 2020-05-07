'''

'''
from scraper_v2 import scraper
from ComputerClass import Computer
import numpy as np
import requests


def write_computer(computer):
    '''
    this function write the infomation of computer into a text file

    **Parameter**
        computer:*object*
            an object that has been initiate by ComputerClass

    **Output**
        None

    **Error**
        AssertionError:*str*
            error if input is not callable
    '''
    try:
        computer.name
    except AttributeError:
        raise AttributeError('The computer is not callable')
    f = open(computer.name + '.txt', 'w')
    f.write(repr(computer))
    f.close()
    print('Saved %s under the same folder' % (computer.name + '.txt'))


def scraper_test():
    '''
    this is a function that test the scraper with buildin link

    **Parameter**
        None

    **Output**
        None

    **Error**
        None
    '''
    url = {
           'test':
           'https://www.newegg.com/CPUs-Processors/Category/ID-34?Tid=6676'
    }
    scraper(url)
    print('Scraper is up and running')


def computer_class_test():
    '''
    This is a function that test to initiate the computerclass

    **Parameter**
        None

    **Output**
        None

    **Error**
        None
    '''
    computer_test = Computer('test')
    print('Computer Builder is up and running')


def meet_requirement(computer, max_price, price_mode, free_shipping):
    '''
    This is a function checks if all the requirement are meet for the computer

    **Parameter**
        computer:*object*
            an object that is initiate by computer class
        max_price:*int/float*
            the max price that you are willing to pay
        price_mode:*str*
            the price mode of the computer built
        free_shipping:*bool*
            if you want free shipping

    **Output**
        True/False:*bool*
            return True if all requirements are met

    **Error**
        AttributeError:
            Error if object is not initiated by ComputerClass
    '''
    try:
        computer.ifcomplete()
    except AttributeError:
        raise AttributeError('Please put in object initiated by ComputerClass')

    if not computer.ifcomplete():
        return False
    compatible = computer.ifcompatible()
    within_price = computer.total_price() <= max_price

    choice = np.random.random() <= 0.9
    low, high = 0, max_price
    if price_mode is 'Cheap' and choice:
        high = max_price / 2
    elif price_mode is 'Expensive' and choice:
        low = max_price / 2
    meet_range = low <= computer.total_price() <= high

    free = computer.total_shipping() == 0
    if compatible and within_price and meet_range:
        if free_shipping:
            if not free:
                return False
        return True
    else:
        return False


def build_a_computer(
                     url,
                     name='MyComputer',
                     max_price=2000,
                     price_mode='Try',
                     free_shipping=False
                    ):
    '''
    This is a function to combine components into computer
    It would try 9999 times to build a computer that meets all the requirement
    before rasing error with 'no possible combinations'
    **Parameters**
        url:*dict,str*
            A dictionary. Keys are component names, hashes are corresponded
            product links from www.newegg.com
        name:*str*
            A str of the name you want to give to the computer
        max_price:*int/float*
            The maximum price you are willing to pay for the computer
        price_mode:*'Try', 'Expensive', 'Cheap'
            The price mode of the computer.
            'Try' represents that you don't have a preference
            'Cheap' means 90% of cases the max price of the computer would be
                less than half of the max_price
            'Expensive' means 90% of cases the min price of the computer would
                be more than half of the max_price
        free_shipping:*bool*
            True means you want free shipping for all components
    **Output**
        YourComputer:*.txt*
            A text file with all the informations of components in you computer
    **Error**
        InputError:*str*
            error if url is not dict
        NameError:*str*
            error if name is not str
        ValueError:*str*
            error if max_price can not be converted into int or float
        PriceModeError:*str*
            error if price_mode doesn't match any of the pre set type
        ShippingError:*str*
            error if free_shipping is not a bool value
        TryError:*str*
            error if 9999 times are tried and
            the computer that meet all requirements is not found
    '''
    assert isinstance(url, dict), 'InputError, url must be a dict'
    assert isinstance(name, str), \
        'NameError, name of the computer should be str'
    try:
        max_price = float(max_price)
    except ValueError:
        raise ValueError('max_price should be numbers')
    assert price_mode in ['Try', 'Cheap', 'Expensive'], \
        'PriceModeError, Wrong price_mode'
    assert isinstance(free_shipping, bool), \
        'ShippingError, attribute free_shipping should be bool'

    component_list = scraper(url)
    computer = Computer(name)
    component_type = computer.component_type
    trytime = 0
    while not meet_requirement(computer, max_price, price_mode, free_shipping):
        for t in component_type:
            t_list = t + '_list'
            if t_list in component_list:
                setattr(computer, t, np.random.choice(component_list[t_list]))
            else:
                setattr(computer, t, 'NA')
        trytime += 1
        assert trytime <= 9999, \
            'TryError, There is no combination that meets all requirement'
    write_computer(computer)


if __name__ == '__main__':
    url = {
        'cpu':
        'https://www.newegg.com/CPUs-Processors/Category/ID-34?Tid=6676',
        'motherboard':
        'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=20',
        'case':
        'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=9',
        'power_supply':
        'https://www.newegg.com/Power-Supplies/Category/ID-32?Tid=6656',
        'memory':
        'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=17',
        'storage':
        'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=15',
        'cooling':
        'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=11',
        'graphic':
        'https://www.newegg.com/p/pl?Submit=StoreIM&Depa=1&Category=38'
    }
    scraper_test()
    computer_class_test()
    build_a_computer(
        url,
        name='BadAssComputer',
        max_price=3000,
        price_mode='Try',
        free_shipping=False
    )
