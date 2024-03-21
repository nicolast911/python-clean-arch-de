# Stater-kit for the refactoring exercise
#
# - Initial version of the invoice generator
# - Currently only supports produce and dairy items
# - We want to extend it to support more departments
# - There are no tests, just a few example inputs (without expected outputs)

# %%
_products = {
    "Lettuce": {"price": 1.00, "department": "Produce"},
    "Onions": {"price": 1.10, "department": "Produce"},
    "Tomatoes": {"price": 1.00, "department": "Produce"},
    "Milk": {"price": 2.50, "department": "Dairy"},
    "Cheese": {"price": 3.00, "department": "Dairy"},
    "Ice Cream": {"price": 3.50, "department": "Dairy"},
    # "Bread": {"price": 1.00, "department": "Bakery"},
    # "Cake": {"price": 10.00, "department": "Bakery"},
    # "Hammer": {"price": 10.00, "department": "Hardware"},
    # "Nails": {"price": 0.10, "department": "Hardware"},
    # "Ladder": {"price": 100.00, "department": "Hardware"},
    # "Drill": {"price": 5.00, "department": "Hardware"},
    # "Xbox": {"price": 250.00, "department": "Electronics"},
    # "TV": {"price": 1000.00, "department": "Electronics"},
    # "Phone": {"price": 800.00, "department": "Electronics"},
}


# %%
_orders = [
    {"customer": "John", "items": [("Lettuce", 2)]},
    {"customer": "Mary", "items": [("Lettuce", 5)]},
    {"customer": "Jill", "items": [("Lettuce", 10)]},
    {"customer": "James", "items": [("Lettuce", 4), ("Onions", 3), ("Tomatoes", 2)]},
    {"customer": "Bob", "items": [("Milk", 2), ("Cheese", 1)]},
    {"customer": "Alice", "items": [("Ice Cream", 5), ("Cheese", 1)]},
    {"customer": "Sam", "items": [("Milk", 4), ("Ice Cream", 4), ("Cheese", 2)]},
    {
        "customer": "Jane's Milky Way",
        "items": [("Cheese", 8), ("Ice Cream", 8), ("Milk", 2)],
    },
]


# %%
def generate_invoice(order, products):
    produce_total, produce_items = 0.0, 0
    dairy_total, dairy_items = 0.0, 0
    result = f"Order for {order['customer']}:\n"
    for item, quantity in order["items"]:
        product = products[item]
        item_price = product["price"]
        department = product["department"]
        if department == "Produce":
            produce_items += quantity
            discount = 0.1 if quantity >= 4 else 0.0
            discounted_price = item_price * (1 - discount)
            price = discounted_price * quantity
            produce_total += price
            result += (
                f"  - {item + ':':12} {quantity:4} à {item_price:3.2f} = ${price:.2f}"
            )
            if discount > 0:
                result += f" (discount: ${item_price * quantity - price:.2f})\n"
            else:
                result += "\n"
        elif department == "Dairy":
            dairy_items += quantity
            discount = 0.05 if quantity >= 5 else 0.0
            discounted_price = item_price * (1 - discount)
            price = discounted_price * quantity
            dairy_total += price
            result += (
                f"  - {item + ':':12} {quantity:4} à {item_price:3.2f} = ${price:.2f}"
            )
            if discount > 0:
                result += f" (discount: ${item_price * quantity - price:.2f})\n"
            else:
                result += "\n"
        else:
            raise ValueError(f"Unknown department: {department}")

    volume_discount = 0.0
    if produce_items >= 10:
        volume_discount += produce_total * 0.05
    if dairy_items >= 10:
        volume_discount += dairy_total * 0.1
    total = produce_total + dairy_total
    if volume_discount > 0:
        result += f"Subtotal:        ${total:.2f}\n"
        result += f"Volume discount: ${volume_discount:.2f}\n"
        result += f"Total:           ${total - volume_discount:.2f}"
    else:
        result += f"Total: ${total:.2f}"
    return result


# %%
if __name__ == "__main__":
    for _order in _orders:
        print(generate_invoice(_order, _products))
        print("=========================================")
