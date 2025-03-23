mn = [      "Pizza", 
      "Burger", "Pasta",     "Salad"]
ord = []

def add(
    ord, c, f   ):
  """Add a new order."""
  if f in mn:
    ord+=[{"customer": c, "food": f}]
    return ord
  

  else:
    print("Item not on the menu.")
    return ord
def get(ord):    return ord

import os


def REMOVE(ord, cus):
  """Remove an order by customer name."""
  ord=[o for o in ord  if o["customer"]!=cus   ]
  return ord

def main() -> None:
    """Main function to demonstrate restaurant order management."""
    Orders = []
    Orders = add(Orders, "Alice", "Pizza")
    Orders = add(Orders,"Bob", "Burger")
    Orders = add(Orders,"Charlie", "Sushi")
    
    print("All Orders:", get(Orders))
    
    Orders = REMOVE(Orders, "Alice")
    print("Orders after removal:", get(Orders))

if __name__ == "__main__":
    main()