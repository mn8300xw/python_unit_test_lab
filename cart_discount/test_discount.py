import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    def test_list_of_two_prices(self):
        prices = [10, 4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_not_a_list_but_integer(self):

        with self.assertRaises(TypeError):
            discount(10)

    def test_discount_empty_list(self):
        self.fail('finish test')

    def test_not_a_list_but_string(self):
        self.fail('must be an integer')

    def test_list_of_different_types(self):
        self.fail('must be an integer list')

    def test_null_input(self):
        self.fail('must have an entry to calculate discount')

    def test_list_of_one_price(self):
        self.fail("This test needs to be implemented")

    # 10
    def test_list_of_negative_prices(self):
        self.fail("This test needs to be implemented")

    # 11 [0 ,0, 0, 0]
    def test_list_of_zeros_prices(self):
        self.fail("This test needs to be implemented")

    # 12
    def test_list_of_floats_prices(self):
        self.fail("This test needs to be implemented")

    # 13
    def test_list_of_mixed_int_and_float_prices(self):
        self.fail("This test needs to be implemented")

    # 14
    def test_all_items_same_price(self):
        self.fail("This test needs to be implemented")

    # 15 Ex: [10000000000000000000000 ** 100000000000000000000000 , 4, 20]
    def test_list_of_large_numbers(self):
        self.fail("This test needs to be implemented")

    # 16 [10 / 0, 4, 20]
    def test_list_with_zero_divisor(self):
        self.fail("This test needs to be implemented")

    # 17 ['0', '4', '20']
    def test_list_with_string_prices(self):
        self.fail("This test needs to be implemented")

if __name__ == '__main__':
    unittest.main()