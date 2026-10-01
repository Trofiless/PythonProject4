import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def products():
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
    return [product1, product2]


@pytest.fixture
def category(products):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни",
        products,
    )


def test_category_creation(category, products):
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category.products == products


def test_product_count(products):
    category = Category("Смартфоны", "Описание", products)
    assert len(category.products) == 2


def test_category_count(products):
    category = Category("Смартфоны", "Описание", products)
    assert category.category_count >= 1


def test_total_product_count(products):
    initial_count = Category.product_count
    Category("Смартфоны", "Описание", products)
    assert Category.product_count == initial_count + 2
