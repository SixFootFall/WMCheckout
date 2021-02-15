from ca.use_cases.product.create_product_use_case import CreateProductUseCase
from ca.use_cases.promotional_rule.create_promotional_rule_use_case import (
    CreatePromotionalRuleUseCase,
)
from ca.repositories.product.memory_repository import MemoryProductRepository
from ca.repositories.promotional_rule.memory_repository import MemoryPromotionalRuleRepository
from ca.entities.checkout import Checkout


class ExampleCheckoutUseCase:
    def __init__(self) -> None:
        self.product_repo = MemoryProductRepository()
        self.rules_repo = MemoryPromotionalRuleRepository()
        self.product_uc = CreateProductUseCase(self.product_repo)
        self.rules_uc = CreatePromotionalRuleUseCase(self.rules_repo)

        self.curry_sauce = self.product_uc.execute("001", "Curry Sauce", 1.95)
        self.pizza = self.product_uc.execute("002", "Pizza", 5.99)
        self.shirt = self.product_uc.execute("003", "Men's T-Shirt", 25.00)

        self.rule_total = self.rules_uc.execute(
            name="If you spend over €30, you get 10 percent off your purchase.",
            discount_type="TOTAL",
            product=None,
            target_quantity=30,
            measure="PERCENTAGE",
            discount_amount=10,
        )

        self.rule_pizza = self.rules_uc.execute(
            name="If you buy 2 or more pizzas, the price for each drops to €3.99.",
            discount_type="PRODUCT",
            product=self.pizza,
            target_quantity=2,
            measure="CURRENCY",
            discount_amount=2,
        )

    def execute(self):

        co = Checkout([self.rule_pizza, self.rule_total])
        co.add(self.pizza)
        co.add(self.curry_sauce)
        co.add(self.pizza)
        co.add(self.shirt)
        total = co.total
        assert total == 31.44
        return total