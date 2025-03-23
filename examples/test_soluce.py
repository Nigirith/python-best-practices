"""Tests for the restaurant order management system."""

from typing import List

import pytest

from .soluce import Order, add_order, get_orders, is_item_on_menu, remove_order


@pytest.fixture
def sample_orders() -> List[Order]:
    """Fixture providing a sample list of orders."""
    return [
        {"customer": "Alice", "food": "Pizza"},
        {"customer": "Bob", "food": "Burger"},
    ]


def test_add_order_valid_food(sample_orders: List[Order]) -> None:
    """Test adding an order with valid food item."""
    orders = add_order(sample_orders, "Charlie", "Pasta")
    assert len(orders) == 3
    assert orders[-1] == {"customer": "Charlie", "food": "Pasta"}


def test_add_order_invalid_food(sample_orders: List[Order]) -> None:
    """Test adding an order with invalid food item."""
    orders = add_order(sample_orders, "Charlie", "Sushi")
    assert len(orders) == 2  # Order should not be added
    assert orders == sample_orders


def test_get_orders(sample_orders: List[Order]) -> None:
    """Test retrieving all orders."""
    orders = get_orders(sample_orders)
    assert len(orders) == 2
    assert orders == sample_orders


def test_remove_order_existing_customer(sample_orders: List[Order]) -> None:
    """Test removing orders for an existing customer."""
    orders = remove_order(sample_orders, "Alice")
    assert len(orders) == 1
    assert all(order["customer"] != "Alice" for order in orders)


def test_remove_order_nonexistent_customer(sample_orders: List[Order]) -> None:
    """Test removing orders for a non-existent customer."""
    orders = remove_order(sample_orders, "NonExistent")
    assert len(orders) == 2
    assert orders == sample_orders


@pytest.mark.parametrize(
    "food,expected",
    [
        ("Pizza", True),
        ("Burger", True),
        ("Pasta", True),
        ("Salad", True),
        ("Sushi", False),
        ("IceCream", False),
    ],
)
def test_is_item_on_menu(food: str, expected: bool) -> None:
    """Test menu item validation with various inputs."""
    assert is_item_on_menu(food) == expected
