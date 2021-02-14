from typing import List
from ca.entities.interfaces import IProduct
from ca.entities.product import Product
import unittest

from ca.repositories.interfaces import IProductRepository
from ca.use_cases.products.create_product_use_case import CreateProductUseCase

from ca.exceptions import UseCaseError


class FakeProductMemoryRepositoryFind(IProductRepository):
    def find_by_code(self, code: str) -> IProduct:
        return Product(code="001", name="Lizard", price=25.99)

    def list(self):
        ...

    def create(self, code: str, name: str, price: float) -> IProduct:
        return Product(code="001", name="Lizard", price=25.99)


class FakeProductMemoryRepositoryCreate(IProductRepository):
    def find_by_code(self, code: str) -> IProduct:
        return None

    def list(self):
        ...

    def create(self, code: str, name: str, price: float) -> IProduct:
        return Product(code="001", name="Lizard", price=25.99)


class TestCreateProductUseCase(unittest.TestCase):
    def test_base_execute(self):
        repo = FakeProductMemoryRepositoryCreate()
        use_case = CreateProductUseCase(repo)
        entity = use_case.execute("001", "Lizard", 25.99)
        self.assertIsInstance(entity, Product)

    def test_duplicate_create(self):
        repo = FakeProductMemoryRepositoryFind()
        use_case = CreateProductUseCase(repo)
        self.assertRaises(UseCaseError, use_case.execute, "001", "Lizard", 25.99)
