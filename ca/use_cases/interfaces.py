from abc import ABCMeta, abstractmethod


class ICreateProductUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, code, name, price):
        pass
