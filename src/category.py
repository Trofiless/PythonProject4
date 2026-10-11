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

        self.__products.append(product)

        Category.product_count += 1

    @property
    def products(self) -> str:

        return "\n".join(
            f"{product.name}, {product.price} руб. "
            f"Остаток: {product.quantity} шт."
            for product in self.__products
        )
