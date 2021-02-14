from ca.entities.interfaces import IProduct


class Product(IProduct):
    def __init__(self, code: str, name: str, price: float):
        if price < 0.01:
            raise ValueError("Price should be more than 1 cent")
        self.code = code
        self.name = name
        self.price = price

    def as_dict(self):
        return {"code": self.code, "name": self.name, "price": self.price}

    @classmethod
    def from_dict(self, adict: dict) -> IProduct:
        product = Product(code=adict["code"], name=adict["name"], price=adict["price"])
        return product

    def __eq__(self, other):
        return self.as_dict() == other.as_dict()

    def __repr__(self):
        return f"""<Product code:{self.code}, name:{self.name}, base price:{self.price}>"""
