import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    INVENTORY = {
        "apple" : 0.4,
        "orange" : 0.8,
        "potato" : 0.2,
    }

    def test_add_item_given_new_item_adds_new_item_to_cart(self):
        sut = ShoppingCart(self.INVENTORY)
        sut.add_item("apple", 8)
        self.assertEqual(sut.items_in_cart, {"apple" : 8})


    def test_add_item_given_multiple_new_items_adds_new_items_to_cart(self):
        sut = ShoppingCart(self.INVENTORY)
        sut.add_item("apple", 8)
        sut.add_item("orange", 1)
        items_in_cart = sut.items_in_cart
        self.assertEqual(items_in_cart, {"apple" : 8, "orange" : 1})


    def test_add_given_item_not_in_database_does_not_update_cart(self):
        sut = ShoppingCart(self.INVENTORY)
        sut.add_item("potato", 10)
        sut.add_item("car", 10)
        sut.add_item("house", 10)
        items_in_cart = sut.items_in_cart
        self.assertEqual(items_in_cart, {"potato" : 10})

    def test_add_item_given_existing_item_increase_qty(self):
        sut = ShoppingCart(self.INVENTORY)
        sut.add_item("apple", 10)
        sut.add_item("apple", 20)
        sut.add_item("apple", 30)
        items_in_cart = sut.items_in_cart
        self.assertEqual(items_in_cart, {"apple": 60})


if __name__ == '__main__':
    unittest.main()