from ca.entities.product import Product
from ca.entities.promotional_rule import PromotionalRule
from ca.repositories.promotional_rule.memory_repository import MemoryPromotionalRuleRepository
from ca.exceptions import PromotionalRuleError
import unittest


class TestPromotionalRuleMemoryRepository(unittest.TestCase):
    def setUp(self):
        self.repo = MemoryPromotionalRuleRepository()
        self.product = Product("001", "Pizza", 90)

    def test_init(self):
        self.assertEqual(self.repo.entities, [])

    def test_create_rule(self):
        rule = self.repo.create(
            name="Test promo rule",
            discount_type="TOTAL",
            product=self.product,
            target_quantity=1,
            measure="PERCENTAGE",
            discount_amount=10,
        )
        self.assertEqual(self.repo.entities, [rule])

    def test_rule_already_exists(self):
        _ = self.repo.create(
            name="Test promo rule",
            discount_type="TOTAL",
            product=self.product,
            target_quantity=1,
            measure="PERCENTAGE",
            discount_amount=10,
        )

        self.assertRaises(
            PromotionalRuleError,
            self.repo.create,
            "Test promo rule",
            "TOTAL",
            self.product,
            1,
            "PERCENTAGE",
            10,
        )
