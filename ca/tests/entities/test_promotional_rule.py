from ca.entities.product import Product
import unittest
from ca.entities.promotional_rule import PromotionalRule
from ca.exceptions import PromotionalRuleError


class TestPromotionalRule(unittest.TestCase):
    def setUp(self) -> None:
        self.product = Product(code="001", name="Lizard", price=25.99)

    def test_product_init(self):
        promo_rule = PromotionalRule(
            name="Test promo rule",
            discount_type="TOTAL",
            product=self.product,
            target_quantity=1,
            measure="PERCENTAGE",
            discount_amount=10,
        )

        self.assertEqual(promo_rule.discount_type, "TOTAL")
        self.assertEqual(promo_rule.target_quantity, 1)
        self.assertEqual(promo_rule.discount_amount, 10)
        self.assertEqual(promo_rule.measure, "PERCENTAGE")
        self.assertEqual(promo_rule.product, self.product)

    def test_fail_init_not_existing_discount_type(self):
        self.assertRaises(
            PromotionalRuleError,
            PromotionalRule,
            "Fail",
            "NOT_EXISTING_TYPE",
            self.product,
            1,
            "PERCENTAGE",
            10,
        )

    def test_discount_more_than_100_percentage(self):
        self.assertRaises(
            PromotionalRuleError,
            PromotionalRule,
            "Fail",
            "TOTAL",
            self.product,
            1,
            "PERCENTAGE",
            101,
        )

    def test_discount_more_product_price(self):
        self.assertRaises(
            PromotionalRuleError,
            PromotionalRule,
            "Fail",
            "PRODUCT",
            self.product,
            1,
            "CURRENCY",
            self.product.price + 1,
        )

    def test_fail_init_not_existing_measurement_type(self):
        self.assertRaises(
            PromotionalRuleError,
            PromotionalRule,
            "Fail",
            "TOTAL",
            self.product,
            1,
            "NOT_EXISTING_MEASURE",
            10,
        )

    def test_fail_init_no_product_with_productbased_type(self):
        self.assertRaises(
            PromotionalRuleError,
            PromotionalRule,
            "Fail",
            "PRODUCT",
            None,
            1,
            "NOT_EXISTING_MEASURE",
            10,
        )

    def test_fail_init_no_product(self):
        self.assertRaises(
            PromotionalRuleError,
            PromotionalRule,
            "Fail",
            "PRODUCT",
            "IMPOSTOR PRODUCT",
            1,
            "NOT_EXISTING_MEASURE",
            10,
        )