from ca.exceptions import PromotionalRuleError
from ca.entities.product import Product
from ca.entities.promotional_rule import PromotionalRule
import unittest
from ca.repositories.interfaces import IPromotionalRuleRepository
from ca.use_cases.promotional_rule.create_promotional_rule_use_case import (
    CreatePromotionalRuleUseCase,
)

fake_product = Product("001", "Pizza", 90)
fake_promo_rule = PromotionalRule(
    name="Test promo rule",
    discount_type="TOTAL",
    product=fake_product,
    target_quantity=1,
    measure="PERCENTAGE",
    discount_amount=10,
)


class FakePromotionalRuleRepoCreate(IPromotionalRuleRepository):
    def create(
        self, name: str, discount_type, product, target_quantity, measure, discount_amount
    ) -> PromotionalRule:
        return fake_promo_rule

    def list(self):
        return []


class FakePromotionalRuleRepoList(IPromotionalRuleRepository):
    def create(
        self, name: str, discount_type, product, target_quantity, measure, discount_amount
    ) -> PromotionalRule:
        ...

    def list(self):
        return [fake_promo_rule]


class TestPromotionalRuleUseCase(unittest.TestCase):
    def test_create(self):
        repo = FakePromotionalRuleRepoCreate()
        use_case = CreatePromotionalRuleUseCase(repo)
        entity = use_case.execute(
            name="Test promo rule",
            discount_type="TOTAL",
            product=fake_product,
            target_quantity=1,
            measure="PERCENTAGE",
            discount_amount=10,
        )
        self.assertIsInstance(entity, PromotionalRule)

    def test_validation(self):
        repo = FakePromotionalRuleRepoList()
        use_case = CreatePromotionalRuleUseCase(repo)

        self.assertRaises(
            PromotionalRuleError,
            use_case.execute,
            "Test promo rule",
            "TOTAL",
            fake_product,
            1,
            "PERCENTAGE",
            10,
        )