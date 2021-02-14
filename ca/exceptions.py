class ProductError(Exception):
    ...


class RepositoryError(ProductError):
    ...


class UseCaseError(ProductError):
    ...


class PromotionalRuleError(Exception):
    ...