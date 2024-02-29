from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity_in_stock: int):
        self.name: str = name
        self.description: str = description
        self._price: float = price
        self.quantity_in_stock: int = quantity_in_stock


    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
