from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ):
        if quantity == 0:
            raise ValueError(
                "Товар с нулевым количеством не может быть добавлен"
            )

        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, product_data: dict):

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __str__(self) -> str:

        return (
            f"{self.name}, {self.price} руб. " f"Остаток: {self.quantity} шт."
        )

    def __add__(self, other: "Product") -> float:

        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного класса")

        return self.price * self.quantity + other.price * other.quantity
