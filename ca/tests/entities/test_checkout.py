import unittest
from ca.entities.product import Product
from ca.entities.promotional_rule import PromotionalRule
from ca.entities.checkout import Checkout


class ProductTest(unittest.TestCase):
    def setUp(self) -> None:
        self.sauce = Product("001", "Curry sauce", 1.95)
        self.pizza = Product("002", "Pizza", 5.99)
        self.shirt = Product("003", "Men's T-Shirt", 25.00)

        self.rule_total = PromotionalRule(
            name="If you spend over €30, you get 10 percent off your purchase.",
            discount_type="TOTAL",
            product=None,
            target_quantity=30,
            measure="PERCENTAGE",
            discount_amount=10,
        )

        self.rule_pizza = PromotionalRule(
            name="If you buy 2 or more pizzas, the price for each drops to €3.99.",
            discount_type="PRODUCT",
            product=self.pizza,
            target_quantity=2,
            measure="CURRENCY",
            discount_amount=2,
        )

        self.rule_pizza_second = PromotionalRule(
            name="If you buy 3 or more pizzas, the price for each drops to €2.99.",
            discount_type="PRODUCT",
            product=self.pizza,
            target_quantity=3,
            measure="CURRENCY",
            discount_amount=3,
        )

        self.rule_one_shirt_discount = PromotionalRule(
            name="If you buy T-Shirt, you are awesome!",
            discount_type="PRODUCT",
            product=self.shirt,
            target_quantity=1,
            measure="PERCENTAGE",
            discount_amount=25,
        )

        self.clean_instance = Checkout([])

    def test_from_example_first(self):
        promotional_rules = [self.rule_pizza, self.rule_total]
        co = Checkout(promotional_rules)
        co.add(self.sauce)
        co.add(self.pizza)
        co.add(self.shirt)
        self.assertEqual(co.total, 29.65)

    def test_from_example_second(self):
        promotional_rules = [self.rule_pizza, self.rule_total]
        co = Checkout(promotional_rules)
        co.add(self.pizza)
        co.add(self.sauce)
        co.add(self.pizza)
        self.assertEqual(co.total, 9.93)

    def test_from_example_third(self):
        promotional_rules = [self.rule_pizza, self.rule_total]
        co = Checkout(promotional_rules)
        co.add(self.pizza)
        co.add(self.sauce)
        co.add(self.pizza)
        co.add(self.shirt)
        self.assertEqual(co.total, 31.44)

    def test_one_rule_one_product(self):
        co = Checkout([self.rule_pizza])
        co.add(self.pizza)
        self.assertEqual(self.pizza.price, co.total)

    def test_one_rule_two_product(self):
        co = Checkout([self.rule_pizza])
        co.add(self.pizza)
        co.add(self.pizza)
        self.assertEqual(7.98, co.total)

    def test_two_rules_two_product(self):
        co = Checkout([self.rule_pizza, self.rule_pizza_second])
        co.add(self.pizza)
        co.add(self.pizza)
        self.assertEqual(7.98, co.total)

    def test_one_rule_three_product(self):
        co = Checkout([self.rule_pizza])
        co.add(self.pizza)
        co.add(self.pizza)
        co.add(self.pizza)
        self.assertEqual(11.97, co.total)

    def test_two_rules_three_product(self):
        co = Checkout([self.rule_pizza, self.rule_pizza_second])
        co.add(self.pizza)
        co.add(self.pizza)
        co.add(self.pizza)
        self.assertEqual(8.97, co.total)

    def test_no_rule_for_product(self):
        co = Checkout([self.rule_one_shirt_discount])
        co.add(self.pizza)
        self.assertEqual(self.pizza.price, co.total)

    def test_percentage_rule_for_product(self):
        co = Checkout([self.rule_one_shirt_discount])
        co.add(self.shirt)
        self.assertEqual(18.75, co.total)

    def test_percentage_rule_for_two_products(self):
        co = Checkout([self.rule_one_shirt_discount])
        co.add(self.shirt)
        co.add(self.shirt)
        self.assertEqual(37.5, co.total)

    def test_checkout_init(self):
        self.assertEqual(self.clean_instance.promotional_rules, [])

    def test_add_one_product(self):
        self.clean_instance.add(self.sauce)
        self.assertEqual(len(self.clean_instance.cart), 1)

    def test_add_two_different_products(self):
        self.clean_instance.add(self.sauce)
        self.clean_instance.add(self.pizza)
        self.assertEqual(len(self.clean_instance.cart), 2)

    def test_add_two_same_products(self):
        self.clean_instance.add(self.sauce)
        self.clean_instance.add(self.sauce)
        self.assertEqual(len(self.clean_instance.cart), 1)

    def test_add_two_same_products(self):
        self.clean_instance.add(self.sauce)
        self.clean_instance.add(self.sauce)
        self.assertEqual(len(self.clean_instance.cart), 1)

    def test_add_two_same_products_quantity(self):
        self.clean_instance.add(self.sauce)
        self.clean_instance.add(self.sauce)
        self.assertEqual(self.clean_instance.cart[self.sauce], 2)

    def test_add_one_product_quantity(self):
        self.clean_instance.add(self.sauce)
        self.assertEqual(self.clean_instance.cart[self.sauce], 1)

    def test_add_one_remove_one_product(self):
        self.clean_instance.add(self.sauce)
        self.clean_instance.remove(self.sauce)
        self.assertEqual(len(self.clean_instance.cart), 0)
        self.assertEqual(self.clean_instance.cart, {})

    def test_remove_empty_cart(self):
        self.assertRaises(ValueError, self.clean_instance.remove, self.sauce)

    def test_add_not_a_product(self):
        self.assertRaises(TypeError, self.clean_instance.add, True)
        self.assertRaises(TypeError, self.clean_instance.add, "Impostor")

    def test_remove_not_a_product(self):
        self.clean_instance.add(self.sauce)
        self.assertRaises(TypeError, self.clean_instance.remove, True)
        self.assertRaises(TypeError, self.clean_instance.remove, "Impostor")

    def test_apply_percentage_discount(self):
        self.assertEqual(Checkout([])._apply_percentage_discount(100, 10), 90)
        self.assertEqual(Checkout([])._apply_percentage_discount(100, 20), 80)
        self.assertEqual(Checkout([])._apply_percentage_discount(100, 50), 50)

    def test_find_rule_by_type(self):
        co = Checkout([self.rule_pizza, self.rule_total])
        result = co._filter_rules_by_type("TOTAL", None, 31)[0]
        self.assertEqual(self.rule_total, result)

    def test_find_rule_by_type_no_rule(self):
        co = Checkout([self.rule_pizza])
        result = co._filter_rules_by_type("TOTAL", None, 31)
        self.assertEqual([], result)

    def test_find_rule_by_type_instance(self):
        co = Checkout([self.rule_pizza, self.rule_total])
        result = co._filter_rules_by_type("TOTAL", None, 31)[0]
        self.assertIsInstance(result, PromotionalRule)

    def test_find_rule_by_type_and_product(self):
        co = Checkout([self.rule_pizza, self.rule_total])
        result = co._filter_rules_by_type("PRODUCT", self.pizza, 2)[0]
        self.assertIsInstance(result, PromotionalRule)

    def test_find_rule_by_type_and_product_no_rule(self):
        co = Checkout([self.rule_pizza, self.rule_total])
        result = co._filter_rules_by_type("PRODUCT", self.pizza, 1)
        self.assertEqual(result, [])
