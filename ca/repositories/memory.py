from ca.repositories.interfaces import IMemoryRepository
from typing import List
from ca.exceptions import RepositoryError
from ca.entities.product import Product


class MemoryRepository(IMemoryRepository):
    def __init__(self, entries=None):
        self._entries = []
        if entries:
            self._entries.extend(entries)

    def find_by_code(self, code):
        for entry in self._entries:
            if entry["code"] == code:
                return Product.from_dict(entry)

    def create(self, code, name, price) -> Product:
        adict = {"code": code, "name": name, "price": price}
        product_entity = Product.from_dict(adict)
        self._entries.append(adict)
        return product_entity

    def list(self) -> List[Product]:
        result = self._entries
        return [Product.from_dict(entry) for entry in result]