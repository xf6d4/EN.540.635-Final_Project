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
                     price_mode='Try',
                     free_shipping=False
                    ):
    def meet_requirement(computer, max_price, price_mode, free_shipping):
        if not computer.ifcomplete():
            return False

        compatible = computer.ifcompatible()
        within_price = bool(computer.get_price() <= max_price)
        low, high = 0, round(max_price)
        if price_mode == 'Cheap':
            high = round(0.5 * max_price)
        elif price_mode == 'Expensive':
            low = round(0.5 * max_price)
        meet_range = bool(computer.get_price() in range(low, high))
        free = bool(computer.total_shipping() == 0)
        if compatible and within_price and meet_range:
            if free_shipping:
                if not free:
                    return False
            return True
        else:
            return False

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
            'There is no combination that meets all requirement'
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
    scraper_test()
    computer_class_test()
    build_a_computer(
        url,
        name='BadAssComputer',
        max_price=2000,
        price_mode='Cheap',
        free_shipping=False
    )
