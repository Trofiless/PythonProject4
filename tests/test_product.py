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
