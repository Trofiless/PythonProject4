import pytest

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


def test_smartphone_creation():

    smartphone = Smartphone(
        "Samsung",
        "Описание",
        1000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    assert smartphone.name == "Samsung"

    assert smartphone.efficiency == 95.5

    assert smartphone.model == "S23 Ultra"

    assert smartphone.memory == 256

    assert smartphone.color == "Серый"


def test_lawn_grass_creation():

    grass = LawnGrass(
        "Газонная трава",
        "Описание",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    assert grass.name == "Газонная трава"

    assert grass.country == "Россия"

    assert grass.germination_period == "7 дней"

    assert grass.color == "Зеленый"


def test_add_smartphones():

    smartphone1 = Smartphone(
        "Samsung", "Описание", 1000.0, 2, 95.5, "S23", 256, "Серый"
    )

    smartphone2 = Smartphone(
        "iPhone", "Описание", 2000.0, 3, 98.2, "15", 512, "Черный"
    )

    assert smartphone1 + smartphone2 == 8000.0


def test_add_lawn_grass():

    grass1 = LawnGrass(
        "Трава 1", "Описание", 100.0, 2, "Россия", "7 дней", "Зеленый"
    )

    grass2 = LawnGrass(
        "Трава 2", "Описание", 200.0, 3, "США", "5 дней", "Темный"
    )

    assert grass1 + grass2 == 800.0


def test_add_different_product_classes():

    smartphone = Smartphone(
        "Samsung", "Описание", 1000.0, 2, 95.5, "S23", 256, "Серый"
    )

    grass = LawnGrass(
        "Трава", "Описание", 100.0, 2, "Россия", "7 дней", "Зеленый"
    )

    with pytest.raises(TypeError):

        smartphone + grass


def test_add_non_product_to_category():

    from src.category import Category

    category = Category("Смартфоны", "Описание", [])

    with pytest.raises(TypeError):

        category.add_product("Not a product")


def test_add_subclass_to_category():

    from src.category import Category

    smartphone = Smartphone(
        "Samsung", "Описание", 1000.0, 2, 95.5, "S23", 256, "Серый"
    )

    category = Category("Смартфоны", "Описание", [])

    category.add_product(smartphone)

    assert "Samsung" in category.products


def test_product_can_be_added_to_category():

    from src.category import Category

    product = Product("Товар", "Описание", 100.0, 2)

    category = Category("Товары", "Описание", [])

    category.add_product(product)

    assert "Товар" in category.products


def test_product_creation_with_zero_quantity():
    with pytest.raises(
        ValueError,
        match="Товар с нулевым количеством не может быть добавлен",
    ):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
