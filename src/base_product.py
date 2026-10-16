from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ):

        self.name = name

        self.description = description

        self.__price = price

        self.quantity = quantity

    @property
    def price(self) -> float:

        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:

        if new_price <= 0:

            print("Цена не должна быть нулевой или отрицательной")

            return

        if new_price < self.__price:

            answer = input("Цена снижается. Подтвердить изменение? (y/n): ")

            if answer.lower() != "y":

                return

        self.__price = new_price

    @abstractmethod
    def __str__(self) -> str:

        pass
