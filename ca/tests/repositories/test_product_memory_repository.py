from ca.exceptions import RepositoryError
import unittest
from ca.entities.product import Product
from ca.repositories.product.memory_repository import MemoryProductRepository


class TestMemoryRepository(unittest.TestCase):
    def setUp(self):
        self.repo = MemoryProductRepository()

    def test_create_product(self):
        adict = {"code": "001", "name": "Lizard", "price": 25.99}
        test_product = self.repo.create(**adict)
        self.assertEqual(test_product, Product.from_dict(adict))

    def test_list_of_products(self):
        adict = {"code": "001", "name": "Lizard", "price": 25.99}
        test_product = self.repo.create(**adict)
        self.assertEqual([test_product], self.repo.list())

    def test_find_by_code(self):
        adict = {"code": "001", "name": "Lizard", "price": 25.99}
        _ = self.repo.create(**adict)
        adict = {"code": "002", "name": "FindThisProduct", "price": 89.99}
        find_this = self.repo.create(**adict)
        self.assertEqual(find_this, self.repo.find_by_code("002"))

    def test_find_nothing_by_code(self):
        self.assertEqual(None, self.repo.find_by_code("CodeDoesNotExist"))

    def test_list_of_null_products(self):
        self.assertEqual([], self.repo.list())
