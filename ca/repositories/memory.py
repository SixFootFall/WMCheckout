from ca.exceptions import RepositoryError
from ca.entities.product import Product


class MemoryRepository:
    def __init__(self, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def _validate(self, product: Product):
        for entry in self._entries:
            if entry["code"] == product.code:
                raise RepositoryError(f'Product with code "{product.code}" already exists')

    def create(self, code, name, price) -> Product:
        adict = {"code": code, "name": name, "price": price}
        product_entity = Product.from_dict(adict)
        self._validate(product_entity)
        self._entries.append(adict)
        return product_entity

    def list(self, filters=None):
        if not filters:
            result = self._entries

        return [Product.from_dict(entry) for entry in result]