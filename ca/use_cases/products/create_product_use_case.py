from ca.entities.interfaces import IProduct
from ca.exceptions import UseCaseError
from ca.use_cases.interfaces import IUseCase


class CreateProductUseCase(IUseCase):
    def __init__(self, repository=None):
        self.repo = repository

    def _validate(self, code):
        if self.repo.find_by_code(code) is not None:
            raise UseCaseError(f"Product with code {code} already exists")

    def execute(self, code, name, price) -> IProduct:
        self._validate(code)
        product = self.repo.create(code, name, price)
        return product