from ca.entities.types import PromoDiscountType, PromoMeasurementsType
from ca.exceptions import PromotionalRuleError
from typing import Optional, Literal
from .product import Product


class PromotionalRule:
    """Promotional rule

    Attributes:
        name:   Meaningful string representation of Promotional rule
        discount_type:  Type of discount. Can be total or product type.
            Total type - Rule applied to total sum
            Product type - Rule applied to specific product
        product:    Product to what rule will be apply.
            Required only if discount type of rule is applying by products
        target_quantity:    On what quantity of products, or sum (based on discount type), rule will be triggered
        measure:    Measure of rule. Can be percentage or currency
        discount_amount:    Amount of rule measure, that will trigger the rule
    """

    def __init__(
        self,
        name: str,
        discount_type: Literal[PromoDiscountType.TOTAL, PromoDiscountType.PRODUCT],
        product: Optional[Product],
        target_quantity: int,
        measure: Literal[PromoMeasurementsType.PERCENTAGE, PromoMeasurementsType.CURRENCY],
        discount_amount: float,
    ) -> None:
        if not PromoDiscountType.has_value(discount_type):
            raise PromotionalRuleError("Not implemented promotional type")
        if not PromoMeasurementsType.has_value(measure):
            raise PromotionalRuleError("Not implemented promotional measure")
        if discount_type == PromoDiscountType.PRODUCT and not isinstance(product, Product):
            raise PromotionalRuleError("No product in product based promotional type")
        if (product and measure == PromoMeasurementsType.CURRENCY) and (
            product.price <= discount_amount
        ):
            raise PromotionalRuleError("Discount amount can not be higher than Product price")
        if measure == PromoMeasurementsType.PERCENTAGE and discount_amount >= 100:
            raise PromotionalRuleError("Discount amount can not be more or equal 100%")
        self.name = name
        self.discount_type = discount_type
        self.product = product
        self.target_quantity = target_quantity
        self.discount_amount = discount_amount
        self.measure = measure

    def __repr__(self) -> str:
        return (
            f"""<Promotional Rule {self.name} type: "{self.discount_type}" """
            + f"""on product "{self.product}" target {self.target_quantity}>"""
        )
