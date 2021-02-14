from abc import ABCMeta, abstractmethod
from ca.entities.types import PromoDiscountType, PromoMeasurementsType
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
        discount_type: Literal[PromoDiscountType.TOTAL, PromoDiscountType.PRODUCT],
        product: Optional[Product],
        target_quantity: int,
        measure: Literal[PromoMeasurementsType.PERCENTAGE, PromoMeasurementsType.CURRENCY],
        discount_amount: float,
    ) -> PromotionalRule:
        ...

    def list(self) -> List[PromotionalRule]:
        ...
