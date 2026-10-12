from src.product import Product


class Category:

    category_count = 0

    product_count = 0

    def __init__(self, name: str, description: str, products: list):

        self.name = name

        self.description = description

        self.__products = []

        for product in products:

            self.add_product(product)

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("В категорию можно добавлять только продукты")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:

        return "\n".join(
            f"{product.name}, {product.price} руб. "
            f"Остаток: {product.quantity} шт."
            for product in self.__products
        )

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)

        return f"{self.name}, количество продуктов: " f"{total_quantity} шт."


def test_category_str(category):

    assert str(category) == "Смартфоны, количество продуктов: 13 шт."
