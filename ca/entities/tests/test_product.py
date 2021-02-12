import unittest
from ca.entities.product import Product


class ProductTest(unittest.TestCase):
    def test_product_init(self):
        product = Product(code="001", name="Lizard", price=25.99)

        self.assertEqual(product.code, "001")
        self.assertEqual(product.name, "Lizard")
        self.assertEqual(product.price, 25.99)

    def test_product_create_from_dict(self):
        adict = {"code": "001", "name": "Lizard", "price": 25.99}
        product = Product.from_dict(adict)
        self.assertEqual(product.code, "001")
        self.assertEqual(product.name, "Lizard")
        self.assertEqual(product.price, 25.99)

    def test_products_equality(self):
        adict = {"code": "001", "name": "Lizard", "price": 25.99}
        product1 = Product.from_dict(adict)
        product2 = Product.from_dict(adict)

        self.assertEqual(product1, product2)
