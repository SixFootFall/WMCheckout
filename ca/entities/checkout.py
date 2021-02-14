from .promotional_rule import PromotionalRule
from .product import Product
from typing import List, Literal, Optional, TypedDict


class CartType(TypedDict):
    Product: int


class Checkout:
    def __init__(self, promotion_rules: List[PromotionalRule]) -> None:
        self.cart: CartType = {}
        self.promotional_rules = promotion_rules

    def add(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError(f"{type(product)} is not instance of Product")
        self.cart[product] = self.cart.get(product, 0) + 1

    def remove(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError(f"{type(product)} is not instance of Product")
        if self.cart.get(product, None) is None:
            raise ValueError(f'No product "{product}" in cart')

        if self.cart.get(product) == 1:
            del self.cart[product]
        else:
            self.cart[product] = self.cart.get(product) - 1

    @staticmethod
    def _apply_percentage_discount(full_price, discount):
        return full_price - (full_price * discount / 100)

    def _filter_rules_by_type(self, rule_type, product, target_quantity):
        filtered_rules = filter(
            lambda x: (x.discount_type == rule_type and x.target_quantity <= target_quantity),
            self.promotional_rules,
        )
        if product and rule_type == "PRODUCT":
            filtered_rules = filter(
                lambda x: (x.product == product),
                filtered_rules,
            )
        return list(filtered_rules)

    def _find_promo_rule(
        self,
        rule_type: Literal["TOTAL", "PRODUCT"],
        product: Optional[CartType],
        target_quantity: float,
    ) -> PromotionalRule:
        filtered_rules = self._filter_rules_by_type(rule_type, product, target_quantity)
        filtered_rules = sorted(filtered_rules, key=lambda x: x.target_quantity)
        fitting_rule = None
        for rule in filtered_rules:
            if target_quantity >= rule.target_quantity:
                fitting_rule = rule
            if target_quantity < rule.target_quantity:
                break
        return fitting_rule

    @staticmethod
    def discounted_value(rule, value_):
        if not rule:
            return value_
        value = value_
        if rule.measure == "CURRENCY":
            value -= rule.discount_amount
        elif rule.measure == "PERCENTAGE":
            value = Checkout._apply_percentage_discount(value, rule.discount_amount)
        return value

    @property
    def total(self):
        total_sum = 0
        for item in self.cart:
            product_discount_rule = self._find_promo_rule("PRODUCT", item, self.cart[item])
            price = self.discounted_value(product_discount_rule, item.price)
            total_sum += price * self.cart[item]

        total_discount_rule = self._find_promo_rule("TOTAL", None, total_sum)
        if total_discount_rule:
            total_sum = self.discounted_value(total_discount_rule, total_sum)
        return total_sum