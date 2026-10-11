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

    return Category("Смартфоны", "Описание категории", products)


def test_category_creation(category):

    assert category.name == "Смартфоны"

    assert category.description == "Описание категории"


def test_products_getter(category):

    result = category.products

    assert "Samsung Galaxy S23 Ultra" in result

    assert "180000.0 руб." in result

    assert "Остаток: 5 шт." in result

    assert "Iphone 15" in result


def test_add_product(category):

    product = Product("Xiaomi", "Синий", 31000.0, 14)

    initial_count = Category.product_count

    category.add_product(product)

    assert "Xiaomi" in category.products

    assert Category.product_count == initial_count + 1


def test_products_are_private(category):

    assert not hasattr(category, "products_list")

    assert hasattr(category, "_Category__products")


def test_category_count(products):

    initial_count = Category.category_count

    Category("Телевизоры", "Описание", products)

    assert Category.category_count == initial_count + 1
