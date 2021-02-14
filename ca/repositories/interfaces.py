from abc import ABCMeta, abstractmethod
from typing import List
from ca.entities.interfaces import IProduct


class IProductRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_code(self, code: str) -> IProduct:
        ...

    @abstractmethod
    def create(self, code: str, name: str, price: float) -> IProduct:
        ...

    @abstractmethod
    def list(self) -> List[IProduct]:
        ...
