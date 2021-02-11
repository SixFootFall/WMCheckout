import unittest
from ca.entities.item import Item


class ItemTest(unittest.TestCase):
    def test_item_init(self):
        item = Item(code="001", name="Lizard", price=25.99)

        self.assertEqual(item.code, "001")
        self.assertEqual(item.name, "Lizard")
        self.assertEqual(item.price, 25.99)

    def test_item_create_from_dict(self):
        adict = {"code": "001", "name": "Lizard", "price": 25.99}
        item = Item.from_dict(adict)
        self.assertEqual(item.code, "001")
        self.assertEqual(item.name, "Lizard")
        self.assertEqual(item.price, 25.99)

    def test_items_equality(self):
        adict = {"code": "001", "name": "Lizard", "price": 25.99}
        item1 = Item.from_dict(adict)
        item2 = Item.from_dict(adict)

        self.assertEqual(item1, item2)
