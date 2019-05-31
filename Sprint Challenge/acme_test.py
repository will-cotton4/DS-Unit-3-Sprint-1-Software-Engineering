#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
    
    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_steal_explode(self):
        """Tests proper response for stealability/explodeability"""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Kinda stealable.')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """Making  sure the reports run properly."""
    def test_default_num_products(self):
        """Tests default number of products being 30."""
        test_list = generate_products()
        self.assertEqual(len(test_list), 30)

    def test_legal_names(self):
        """Tests generated names to make sure they're 'legal.'"""
        test_list = generate_products()
        for prod in test_list:
            name = prod.name
            split_name = name.split()
            test_adj = split_name[0]
            test_noun = split_name[1]
            self.assertIn(test_adj, ADJECTIVES)
            self.assertIn(' ', name)
            self.assertIn(test_noun, NOUNS)

            
if __name__ == '__main__':
    unittest.main()