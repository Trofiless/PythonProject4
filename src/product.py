class Product:

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
    def price(self):

        return self.__price

    @price.setter
    def price(self, new_price: float):

        if new_price <= 0:

            print("Цена не должна быть нулевая или отрицательная")

            return

        if new_price < self.__price:

            answer = input("Цена снижается. Подтвердить изменение? (y/n): ")

            if answer.lower() != "y":

                return

        self.__price = new_price

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
