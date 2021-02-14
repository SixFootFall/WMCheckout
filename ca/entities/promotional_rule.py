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

    TYPES = (
        "TOTAL",
        "PRODUCT",
    )
    MEASUREMENTS = (
        "PERCENTAGE",
        "CURRENCY",
    )

    def __init__(
        self,
        name: str,
        discount_type: Literal["TOTAL", "PRODUCT"],
        product: Optional[Product],
        target_quantity: int,
        measure: Literal["PERCENTAGE", "CURRENCY"],
        discount_amount: float,
    ) -> None:
        if discount_type not in PromotionalRule.TYPES:
            raise PromotionalRuleError("Not implemented promotional type")
        if measure not in PromotionalRule.MEASUREMENTS:
            raise PromotionalRuleError("Not implemented promotional measure")
        if discount_type == "PRODUCT" and not isinstance(product, Product):
            raise PromotionalRuleError("No product in product based promotional type")

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
