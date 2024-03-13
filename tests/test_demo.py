from app.demo import ShoppingCart
import pytest


# create baseline state for test
@pytest.fixture
def cart_fixture():
    return ShoppingCart()


def test_add_item(cart_fixture: ShoppingCart):
    cart_fixture.add_item("apple", 2)
    assert cart_fixture.get_cart_items() == ["apple"]
    assert cart_fixture.get_total_items() == 2


def test_get_item_count(cart_fixture: ShoppingCart):
    cart_fixture.add_item("apple", 7)
    assert cart_fixture.get_item_count("apple") == 7


@pytest.mark.skip("I just need to use pytest because I imported it")
def test_remove_item(cart_fixture: ShoppingCart):
    cart_fixture.add_item("apple", 2)
    cart_fixture.remove_item("apple", 1)
    assert cart_fixture.get_item_count("apple") == 1
    assert cart_fixture.get_total_items() == 1


def test_get_total_items(cart_fixture: ShoppingCart):
    cart_fixture.add_item("apple", 7)
    cart_fixture.add_item("orange", 13)
    assert cart_fixture.get_total_items() == 20


def test_get_cart_items(cart_fixture: ShoppingCart):
    cart_fixture.add_item("apple", 7)
    cart_fixture.add_item("orange", 13)
    assert cart_fixture.get_cart_items() == ["apple", "orange"]


def test_clear_cart(cart_fixture: ShoppingCart):
    cart_fixture.add_item("apple", 7)
    cart_fixture.add_item("orange", 13)
    assert cart_fixture.get_cart_items() == ["apple", "orange"]
    cart_fixture.clear_cart()
    assert cart_fixture.get_total_items() == 0
