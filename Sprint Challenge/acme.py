'''
This module includes the definition of
a Product class.
'''

import random


class Product():
    '''
    Models products.

    Parameters
    -----------------------------
    name : string
        name of product
    price : int
        price of product in dollars, default 10
    weight : int
        weight of product in pounds, default 20
    flammability : float
        flammmability of product in flames, default 0.5

    Attributes
    -----------------------------

    Methods
    -----------------------------
    stealability(self): calculates the price divided by the weight, and
    then returns a message: if the ratio is less than 0.5 return "Not
    so stealable...", if it is greater or equal to 0.5 but less than
    1.0 return "Kinda stealable.", and otherwise return "Very
    stealable!"

    explode(self): calculates the flammability times the weight, and
    then returns a message: if the product is less than 10 return
    "...fizzle.", if it is greater or equal to 10 but less than 50
    return "...boom!", and otherwise return "...BABOOM!!"
    '''
    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 10000000)):
                self.name = name
                self.price = price
                self.weight = weight
                self.flammability = flammability
                self.identifier = identifier

    def stealability(self):
        steal_ratio = self.price/self.weight
        stealability = 'default'
        if(steal_ratio < 0.5):
            stealability = 'Not so stealable...'
        elif(0.5 <= steal_ratio < 1):
            stealability = 'Kinda stealable.'
        else:
            stealability = 'Very stealable!'
        return stealability

    def explode(self):
        explosivity = self.flammability*self.weight
        explode_message = 'default'
        if(explosivity < 10):
            explode_message = '...fizzle.'
        elif(10 <= explosivity < 50):
            explode_message = '...boom!'
        else:
            explode_message = '...BABOOM!!'
        return explode_message


class BoxingGlove(Product):
    '''
    Models a boxing glove (inherited from product).

    Parameters
    -----------------------------
    name : string
        name of product
    price : int
        price of product in dollars, default 10
    weight : int
        weight of product in pounds, default 10
    flammability : float
        flammmability of product in flames, default 0.5

    Attributes
    -----------------------------

    Methods
    -----------------------------
    stealability(self): calculates the price divided by the weight, and
    then returns a message: if the ratio is less than 0.5 return "Not
    so stealable...", if it is greater or equal to 0.5 but less than
    1.0 return "Kinda stealable.", and otherwise return "Very
    stealable!"

    explode(self): ...it's a glove.

    punch(self): returns "That tickles." if the weight is below 5,
    "Hey that hurt!" if the weight is greater or equal to 5 but less
    than 15, and "OUCH!" otherwise.
    '''
    def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 10000000)):
                Product.__init__(self, name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        punchable = 'default'
        if(self.weight < 5):
            punchable = 'That tickles.'
        elif(5 <= self.weight < 15):
            punchable = 'Hey that hurt!'
        else:
            punchable = 'OUCH!'
        return punchable
