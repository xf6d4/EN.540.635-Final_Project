from scraper_v2 import scraper
from ComputerClass import Computer
import numpy as np

if __name__ == '__main__':
    component_list = scraper()
    computer = Computer('BadAssComputer')
    component_type = list(computer.__dict__.keys())
    for t in component_type:
        t_list = t + '_list'
        if t_list in component_list and component_list[t_list] != []:
            setattr(computer, t, np.random.choice(component_list[t_list]))
            # computer.t = np.random.choice(component_list[t_list])
        else:
            setattr(computer, t, 'NA')
            # computer.t = "NA"
    print(repr(computer))
