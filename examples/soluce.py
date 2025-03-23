from typing import List, TypedDict

class Order(TypedDict):
    customer: str
    food: str

MENU = ["Pizza", "Burger", "Pasta", "Salad"]

def add_order(orders:List[Order], customer: str, food: str) -> List[Order]:
    """Add a new order if the food is on the menu."""
    if food in MENU:
        orders+=[{"customer": customer, "food": food}]
        return orders
    print(f"Error: {food} is not on the menu.")
    return orders

def get_orders(orders:List[Order]) -> List[Order]:
    """Return the list of all orders."""
    return orders

def remove_order(orders:List[Order], customer: str) -> None:
    """Remove all orders for a given customer."""
    return [order for order in orders if order["customer"] != customer]

def is_item_on_menu(food: str) -> bool:
    """Check if a food item is on the menu."""
    return food in MENU


def main() -> None:
    """Main function to demonstrate restaurant order management."""
    food_by_customer: List[Order] = []
    food_by_customer = add_order(food_by_customer, "Alice", "Pizza")
    food_by_customer = add_order(food_by_customer,"Bob", "Burger")
    food_by_customer = add_order(food_by_customer,"Charlie", "Sushi")
    
    print("All Orders:", get_orders(food_by_customer))
    
    remove_order(food_by_customer, "Alice")
    print("Orders after removal:", get_orders(food_by_customer))

if __name__ == "__main__":
    main()