'''
Created on May, 2
Classes that build a computer from components provided by ComponentClass
and check if components are applicable

@author LT_LUTUO
@coauthor: xf6d4
'''


class Computer(object):
    '''
    This is a class to build computers
    there are subfunctions to check its compatibility and calculate its price
    '''
    def __init__(
                self, name='MyComputer', cpu=None, motherboard=None, case=None,
                power_supply=None, memory=None, storage=None, cooling=None,
                graphic=None, os=None, monitor=None, mice=None, keyboard=None
                ):
        '''
        initiate the computer with its component

        **Parameters**
            name:*str*
                Name of the computer
            cpu:*object*
                cpu for the computer
            motherboard:*object*
                motherboard for the computer
            case:*object*
                case for the computer
            power_supply:*object*
                power_supply for the computer
            memory:*object*
                memory for the computer
            storage:*object*
                storage for the computer
            cooling:*object*
                cooling for the computer
            graphic:*object*
                graphic for the computer
            os:*object*
                os for the computer
            monitor:*object*
                monitor for the computer
            mice:*object*
                mice for the computer
            keyboard:*object*
                keyboard for the computer

        **Output**
            None

        **Error**
            None
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
        '''
        this function return an overview of the computer
        **Parameter**
            None

        **Output**
            msg:*str*
                str of component info of the computer

        **Error**
            None
        '''
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

    def __call__(self):
        '''
        This return the name of the computer
        **Output**
            name:*str*
                str of name of the computer
        '''
        return self.name

    def __repr__(self):
        '''
        This return all information of the computer
        **Parameter**
            None

        **Output**
            msg:*str*
                detail information for all components in the computer

        **Error**
            None
        '''
        msg = "%s:%r\n%s:%r\n%s:%r\n%s:%r\n%s:%r\n%s:%r\n%s:%r\n%s:%r\n%s:%r \
               \n%s:%r\n%s:%r\n%s:%r\n%s:%r\n%s:$%.2f\n%s:$%.2f" \
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
        '''
        This function checks if the cpu and motherboard are compatible

        **Output**
            True/False:*bool*
                return true if cpu is compatible with motherboard
        **Error**
            CallableError:
                return error if cpu.brand or motherboard.detail is not callable
        '''
        assert callable(self.cpu.brand) and callable(self.motherboard.detail),\
            'CPU or Motherboard should not be empty' \
            'if compatible check is needed'
        if self.cpu.brand not in self.motherboard.detail:
            return False
        return True

    def ifcomplete(self):
        '''
        check if all the components are not None
        **Output**
            check:*bool*
                True if all the components are not None
        **Error**
            None
        '''
        check = any([self.__dict__[c] for c in self.component_type])
        return check

    def get_price(self):
        price = 0
        for t in self.component_type:
            c = self.__dict__[t]
            if type(c) != str:
                try:
                    float(c.price)
                except ValueError:
                    pass
                else:
                    price += float(c.price)
        return price

    def total_shipping(self):
        shipping = 0
        for t in self.component_type:
            c = self.__dict__[t]
            if type(c) != str:
                try:
                    float(c.shipping)
                except ValueError:
                    pass
                else:
                    shipping += float(c.shipping)
        return shipping
