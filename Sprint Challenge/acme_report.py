'''
This module includes two functions and two global constants:

Functions
-----------------------------
generate_products()
Generates a given number of products and returns them as a list

inventory_report()
Takes a list of products and prints a summary

Constants
-----------------------------
ADJECTIVES
a list of adjectives to apply to products

NOUNS
a list of nouns describing products
'''

import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']

NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    product_list = []
    for _ in range(num_products):
        adj_index = random.randint(0, len(ADJECTIVES)-1)
        noun_index = random.randint(0, len(NOUNS)-1)
        name = ADJECTIVES[adj_index] + " " + NOUNS[noun_index]
        price = random.randint(5, 101)
        weight = random.randint(5, 101)
        flammability = random.uniform(0, 2.5)
        product_list.append(Product(name=name, price=price, weight=weight,
                            flammability=flammability))
    return product_list


def inventory_report(prods):
    mean_price = sum([prod.weight for prod in prods])/len(prods)
    mean_weight = sum([prod.price for prod in prods])/len(prods)
    mean_flammability = sum([prod.flammability for prod in prods])/len(prods)
    num_unique_prod = len(set(prods))  # Sets only count uniques once
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:", num_unique_prod)
    print("Average price:", mean_price)
    print("Average weight:", mean_weight)
    print("Average flammability:", mean_flammability)


if __name__ == '__main__':
    inventory_report(generate_products())
