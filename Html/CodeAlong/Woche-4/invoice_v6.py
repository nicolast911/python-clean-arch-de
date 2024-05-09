# invoice_v6.py:
#
# Generalize for multiple departments/cleanup of `add_line_for_single_item()`
#
# - Introduce missing abstraction for departments
# - Introduce missing abstraction for single department statistics

import io
import pytest

_departments = {
    "Produce": {"min_items_for_discount": 4, "discount": 0.1},
    "Dairy": {"min_items_for_discount": 5, "discount": 0.05},
}

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


class DepartmentStatistics:
    def __init__(self):
        self.department_stats = {}

    def __getitem__(self, item):
        return self.department_stats.setdefault(item, {"items": 0, "total": 0.0})


def generate_invoice(order, products):
    department_stats = DepartmentStatistics()
    result = io.StringIO()
    result.write(f"Order for {order['customer']}:\n")
    for line_item in order["items"]:
        add_line_for_single_item(department_stats, line_item, products, result)

    add_volume_discount(department_stats, result)
    return result.getvalue()


def add_line_for_single_item(
    department_stats: DepartmentStatistics, line_item: tuple[str, int], products, result
):
    item, quantity = line_item
    product = products[item]
    item_price = product["price"]
    department_name = product["department"]
    if department_name == "Produce":
        department_stats[department_name]["items"] += quantity
        discount = compute_department_discount(department_name, quantity)
        discounted_price = item_price * (1 - discount)
        price = discounted_price * quantity
        department_stats[department_name]["total"] += price
        result.write(
            f"  - {item + ':':12} {quantity:4} à {item_price:3.2f} = ${price:.2f}"
        )
        if discount > 0:
            result.write(f" (discount: ${item_price * quantity - price:.2f})\n")
        else:
            result.write("\n")
    elif department_name == "Dairy":
        department_stats[department_name]["items"] += quantity
        discount = compute_department_discount(department_name, quantity)
        discounted_price = item_price * (1 - discount)
        price = discounted_price * quantity
        department_stats[department_name]["total"] += price
        result.write(
            f"  - {item + ':':12} {quantity:4} à {item_price:3.2f} = ${price:.2f}"
        )
        if discount > 0:
            result.write(f" (discount: ${item_price * quantity - price:.2f})\n")
        else:
            result.write("\n")
    else:
        raise ValueError(f"Unknown department: {department_name}")


def compute_department_discount(department_name, quantity):
    department = _departments[department_name]
    if quantity >= department["min_items_for_discount"]:
        return department["discount"]
    else:
        return 0.0


def add_volume_discount(department_stats: DepartmentStatistics, result):
    volume_discount = 0.0
    if department_stats["Produce"]["items"] >= 10:
        volume_discount += department_stats["Produce"]["total"] * 0.05
    if department_stats["Dairy"]["items"] >= 10:
        volume_discount += department_stats["Dairy"]["total"] * 0.1
    total = department_stats["Produce"]["total"] + department_stats["Dairy"]["total"]
    if volume_discount > 0:
        result.write(f"Subtotal:        ${total:.2f}\n")
        result.write(f"Volume discount: ${volume_discount:.2f}\n")
        result.write(f"Total:           ${total - volume_discount:.2f}")
    else:
        result.write(f"Total: ${total:.2f}")


if __name__ == "__main__":
    for _order in _orders:
        print(generate_invoice(_order, _products))
        print("=========================================")


@pytest.mark.parametrize("order", _orders)
def test_generate_invoice(order):
    from invoice_v0 import generate_invoice as golden_master

    result = generate_invoice(order, _products)

    assert result == golden_master(order, _products)
