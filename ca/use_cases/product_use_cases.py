from ca.entities.product import Product
from .interfaces import ICreateProductUseCase


class CreateProductUseCase(ICreateProductUseCase):
    def __init__(self, repository=None):
        self.repo = repository

    def execute(self, code, name, price):
        product = Product(code=code, name=name, price=price)
        return self.repo.create(product)