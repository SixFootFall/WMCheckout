from ca.entities.types import PromoDiscountType, PromoMeasurementsType
from typing import Literal, Optional

from ca.entities.product import Product
from ca.entities.promotional_rule import PromotionalRule
from ca.exceptions import PromotionalRuleError
from ca.repositories.interfaces import IPromotionalRuleRepository
from ca.use_cases.interfaces import IUseCase


class CreatePromotionalRuleUseCase(IUseCase):
    def __init__(self, repository: IPromotionalRuleRepository = None):
        self.repo = repository

    def _validate(self, discount_type, product, target_quantity):
        for entity in self.repo.list():
            if (
                entity.discount_type == discount_type
                and entity.product == product
                and entity.target_quantity == target_quantity
            ):
                raise PromotionalRuleError(
                    f"""Rule with type:{discount_type}, 
                        product:{product}, 
                        target_quantity: {target_quantity} 
                        already exists in repository"""
                )

    def execute(
        self,
        name: str,
        discount_type: Literal[PromoDiscountType.TOTAL, PromoDiscountType.PRODUCT],
        product: Optional[Product],
        target_quantity: int,
        measure: Literal[PromoMeasurementsType.PERCENTAGE, PromoMeasurementsType.CURRENCY],
        discount_amount: float,
    ) -> PromotionalRule:
        self._validate(
            discount_type=discount_type, product=product, target_quantity=target_quantity
        )
        rule = self.repo.create(
            name, discount_type, product, target_quantity, measure, discount_amount
        )
        return rule
