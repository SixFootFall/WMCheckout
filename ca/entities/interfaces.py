from abc import ABCMeta, abstractmethod, abstractproperty, abstractclassmethod


class IProduct(metaclass=ABCMeta):
    @abstractclassmethod
    def from_dict(self, adict: dict) -> "IProduct":
        ...

    @abstractmethod
    def as_dict(self) -> dict:
        ...
