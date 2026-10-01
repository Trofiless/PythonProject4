import pytest

from src.category import Category

from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counters():

    Category.category_count = 0

    Category.product_count = 0


def test_category_creation():

    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )

    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
    )

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )

    assert category.name == "Смартфоны"

    assert category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )

    assert category.products == [product1, product2]


def test_category_count():

    product = Product("Телефон", "Описание", 100000.0, 5)

    Category("Смартфоны", "Описание", [product])

    Category("Телевизоры", "Описание", [product])

    assert Category.category_count == 2


def test_product_count():

    product1 = Product("Телефон", "Описание", 100000.0, 5)

    product2 = Product("Ноутбук", "Описание", 150000.0, 3)

    product3 = Product("Телевизор", "Описание", 80000.0, 2)

    Category("Смартфоны", "Описание", [product1, product2])

    Category("Телевизоры", "Описание", [product3])

    assert Category.product_count == 3
