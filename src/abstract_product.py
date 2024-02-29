from abc import ABC, abstractmethod


class AbstractProduct(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
