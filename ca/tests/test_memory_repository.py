from ca.exceptions import RepositoryError
import unittest
from ca.entities.product import Product
from ca.repositories.memory import MemoryRepository


class MemoryRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.repo = MemoryRepository()

    def test_create_product(self):
        adict = {"code": "001", "name": "Lizard", "price": 25.99}
        test_product = self.repo.create(**adict)
        self.assertEqual(test_product, Product.from_dict(adict))

    def test_list_of_null_products(self):
        self.assertEqual([], self.repo.list())

    def test_list_of_null_products(self):
        adict = {"code": "001", "name": "Lizard", "price": 25.99}
        test_product = self.repo.create(**adict)
        self.assertEqual([test_product], self.repo.list())

    def test_create_product_twice(self):
        adict = {"code": "001", "name": "Lizard", "price": 25.99}
        test_product = self.repo.create(**adict)
        self.assertRaises(
            RepositoryError,
            self.repo.create,
            "001",
            "Lizard",
            231,
        )
