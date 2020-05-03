from scraper_v2 import scraper
from ComputerClass import Computer
import numpy as np


def scraper_test():
    url = {
           'test':
           'https://www.newegg.com/CPUs-Processors/Category/ID-34?Tid=6676'
    }
    scraper(url)
    print('Scraper is up and running')


def computer_class_test():
    computer_test = Computer('test')
    print('Computer Builder is up and running')


def build_a_computer(
                     url,
                     name='MyComputer',
                     max_price=2000,
                     price_mode='try',
                     shipping=False
                    ):
    def if_meet_requirement():
        pass
    component_list = scraper(url)
    for i in component_list:
        if component_list[i] == []:
            raise AssertionError('Something is wrong with the link for %s' % i)
    computer = Computer(name)
    component_type = computer.component_type
    compatible = False
    while not compatible:
        for t in component_type:
            t_list = t + '_list'
            if t_list in component_list and component_list[t_list] != []:
                setattr(computer, t, np.random.choice(component_list[t_list]))
            else:
                setattr(computer, t, 'NA')
        compatible = computer.ifcompatible()
    print(repr(computer))


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
    component_list = scraper_test()
    computer_class_test()
    build_a_computer(
        url,
        name='BadAssComputer',
        max_price=2000,
        price_mode='try',
        shipping=False
    )
