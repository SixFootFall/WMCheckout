from abc import ABCMeta, abstractmethod
from ca.entities.product import Product
from ca.entities.promotional_rule import PromotionalRule
from typing import List, Literal, Optional
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


class IPromotionalRuleRepository(metaclass=ABCMeta):
    def create(
        self,
        name: str,
        discount_type: Literal["TOTAL", "PRODUCT"],
        product: Optional[Product],
        target_quantity: int,
        measure: Literal["PERCENTAGE", "CURRENCY"],
        discount_amount: float,
    ) -> PromotionalRule:
        ...

    def list(self) -> List[PromotionalRule]:
        ...
