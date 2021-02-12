from ca.entities.product import Product


class ProductError(Exception):
    ...


class RepositoryError(ProductError):
    ...


class UseCaseError(ProductError):
    ...
