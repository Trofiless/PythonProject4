import pytest

from src.product import Product


@pytest.fixture
def product():

    return Product("Samsung", "Серый цвет", 180000.0, 5)


def test_product_creation(product):

    assert product.name == "Samsung"

    assert product.description == "Серый цвет"

    assert product.price == 180000.0

    assert product.quantity == 5


def test_price_getter(product):

    assert product.price == 180000.0


def test_price_setter(product):

    product.price = 190000.0

    assert product.price == 190000.0


def test_price_setter_rejects_zero(product):

    product.price = 0

    assert product.price == 180000.0


def test_price_setter_rejects_negative(product):

    product.price = -100

    assert product.price == 180000.0


def test_price_setter_requires_confirmation(product, monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "n")

    product.price = 170000.0

    assert product.price == 180000.0


def test_price_setter_accepts_confirmation(product, monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "y")

    product.price = 170000.0

    assert product.price == 170000.0


def test_new_product():

    product = Product.new_product(
        {
            "name": "iPhone",
            "description": "512GB",
            "price": 210000.0,
            "quantity": 8,
        }
    )

    assert isinstance(product, Product)

    assert product.name == "iPhone"

    assert product.description == "512GB"

    assert product.price == 210000.0

    assert product.quantity == 8


def test_product_str():

    product = Product("Samsung", "Описание", 100.0, 5)

    assert str(product) == "Samsung, 100.0 руб. Остаток: 5 шт."


def test_product_add():

    product1 = Product("Товар 1", "Описание", 100.0, 10)

    product2 = Product("Товар 2", "Описание", 200.0, 2)

    assert product1 + product2 == 1400.0
