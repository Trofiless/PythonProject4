from src.category import Category
from src.product import Product


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
        "Смартфоны как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2],
    )
    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category.products == [product1, product2]
