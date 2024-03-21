# invoice_v10.py:
#
# - Enable other departments
# - Add example order with items from other departments
# - Add additional test for other departments
# - Change output format (needs updates to tests)

import io
from dataclasses import dataclass, field

import pytest


@dataclass
class Department:
    name: str
    min_items_for_discount: int
    discount: float
    min_items_for_volume_discount: int
    volume_discount: float


_departments = {
    "Produce": Department(
        name="Produce",
        min_items_for_discount=4,
        discount=0.1,
        min_items_for_volume_discount=10,
        volume_discount=0.05,
    ),
    "Dairy": Department(
        name="Dairy",
        min_items_for_discount=5,
        discount=0.05,
        min_items_for_volume_discount=10,
        volume_discount=0.1,
    ),
    "Bakery": Department(
        name="Bakery",
        min_items_for_discount=3,
        discount=0.1,
        min_items_for_volume_discount=6,
        volume_discount=0.05,
    ),
    "Hardware": Department(
        name="Hardware",
        min_items_for_discount=5,
        discount=0.1,
        min_items_for_volume_discount=3,
        volume_discount=0.1,
    ),
    "Electronics": Department(
        name="Electronics",
        min_items_for_discount=5,
        discount=0.02,
        min_items_for_volume_discount=15,
        volume_discount=0.02,
    ),
}


@dataclass(init=False)
class Product:
    price_per_item: float
    department: Department

    def __init__(self, price: float, department: str):
        self.price_per_item = price
        self.department = _departments[department]

    def discount(self, quantity):
        department: Department = self.department
        if quantity >= department.min_items_for_discount:
            return department.discount
        else:
            return 0.0

    def discounted_price_per_item(self, quantity):
        discount = self.discount(quantity)
        return self.price_per_item * (1 - discount)

    def total_price(self, quantity):
        return self.discounted_price_per_item(quantity) * quantity

    def total_discount(self, quantity):
        return self.price_per_item * quantity - self.total_price(quantity)


_products = {
    "Lettuce": Product(price=1.00, department="Produce"),
    "Onions": Product(price=1.10, department="Produce"),
    "Tomatoes": Product(price=1.00, department="Produce"),
    "Milk": Product(price=2.50, department="Dairy"),
    "Cheese": Product(price=3.00, department="Dairy"),
    "Ice Cream": Product(price=3.50, department="Dairy"),
    "Bread": Product(price=1.00, department="Bakery"),
    "Cake": Product(price=10.00, department="Bakery"),
    "Hammer": Product(price=10.00, department="Hardware"),
    "Nails": Product(price=0.10, department="Hardware"),
    "Ladder": Product(price=100.00, department="Hardware"),
    "Drill": Product(price=5.00, department="Hardware"),
    "Xbox": Product(price=250.00, department="Electronics"),
    "TV": Product(price=1000.00, department="Electronics"),
    "Phone": Product(price=800.00, department="Electronics"),
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
    {
        "customer": "Dave's Emporium",
        "items": [
            ("Hammer", 5),
            ("Nails", 100),
            ("Ladder", 1),
            ("Drill", 5),
            ("Xbox", 2),
            ("TV", 5),
            ("Phone", 8),
        ],
    },
]


@dataclass
class DepartmentStats:
    items: int = 0
    total: float = 0.0


@dataclass
class OrderTracker:
    customer: str
    products: dict[str, Product]
    _department_stats_dict: dict[str, DepartmentStats] = field(
        default_factory=dict, init=False
    )
    _line_items: list[tuple[str, int, Product]] = field(
        default_factory=list, init=False
    )

    def get_department_stats(self, department_name):
        return self._department_stats_dict.setdefault(
            department_name, DepartmentStats()
        )

    def add_line_item(self, line_item: tuple[str, int]):
        item, quantity = line_item
        product: Product = self.products[item]
        self._register_sale_for_department(product, quantity)
        self._line_items.append((item, quantity, product))

    def _register_sale_for_department(self, product, quantity):
        price = product.total_price(quantity)
        department_stats = self.get_department_stats(product.department.name)
        department_stats.items += quantity
        department_stats.total += price

    @property
    def result(self):
        result: io.StringIO = io.StringIO()
        result.write(f"Order for {self.customer}:\n")
        for item, quantity, product in self._line_items:
            self._print_line_item(item, quantity, product, result)
        self._print_volume_discount_and_total(result)

        return result.getvalue()

    @staticmethod
    def _print_line_item(item, quantity, product, result):
        result.write(
            f"  - {item + ':':12} {quantity:4} à {product.price_per_item :>7.2f} "
            f"= {product.total_price(quantity):>7.2f}"
        )
        if product.discount(quantity) > 0:
            result.write(f" (discount: {product.total_discount(quantity):>7.2f})\n")
        else:
            result.write("\n")

    def _print_volume_discount_and_total(self, result):
        total = 0.0
        volume_discount = 0.0
        for department_name, department in _departments.items():
            department_stats = self.get_department_stats(department_name)
            if department_stats.items >= department.min_items_for_volume_discount:
                volume_discount += department_stats.total * department.volume_discount
            total += department_stats.total

        if volume_discount > 0:
            result.write(f"Subtotal:        {total:>7.2f}\n")
            result.write(f"Volume discount: {volume_discount:>7.2f}\n")
            result.write(f"Total:           {total - volume_discount:>7.2f}")
        else:
            result.write(f"Total: {total:.2f}")


def generate_invoice(order, products):
    order_tracker: OrderTracker = OrderTracker(order["customer"], products)
    for line_item in order["items"]:
        order_tracker.add_line_item(line_item)

    return order_tracker.result


if __name__ == "__main__":
    for _order in _orders:
        print(generate_invoice(_order, _products))
        print("=========================================")


_test_cases = [
    (
        {"customer": "John", "items": [("Lettuce", 2)]},
        ["Order for John:", "- Lettuce: 2 à 1.00 = 2.00", "Total: 2.00"],
    ),
    (
        {"customer": "Mary", "items": [("Lettuce", 5)]},
        [
            "Order for Mary:",
            "  - Lettuce:    5 à 1.00 = 4.50 (discount: 0.50)",
            "Total: 4.50",
        ],
    ),
    (
        {"customer": "Jill", "items": [("Lettuce", 10)]},
        [
            "Order for Jill:",
            "  - Lettuce:    10 à 1.00 = 9.00 (discount: 1.00)",
            "Subtotal:        9.00",
            "Volume discount: 0.45",
            "Total:           8.55",
        ],
    ),
    (
        {
            "customer": "James",
            "items": [("Lettuce", 4), ("Onions", 3), ("Tomatoes", 2)],
        },
        [
            "Order for James:",
            "  - Lettuce:        4 à 1.00 = 3.60 (discount: 0.40)",
            "  - Onions:         3 à 1.10 = 3.30",
            "  - Tomatoes:       2 à 1.00 = 2.00",
            "Total: 8.90",
        ],
    ),
    (
        {"customer": "Bob", "items": [("Milk", 2), ("Cheese", 1)]},
        [
            "Order for Bob:",
            "  - Milk:           2 à 2.50 = 5.00",
            "  - Cheese:         1 à 3.00 = 3.00",
            "Total: 8.00",
        ],
    ),
    (
        {"customer": "Alice", "items": [("Ice Cream", 5), ("Cheese", 1)]},
        [
            "Order for Alice:",
            "  - Ice Cream:      5 à 3.50 = 16.62 (discount: 0.88)",
            "  - Cheese:         1 à 3.00 = 3.00",
            "Total: 19.62",
        ],
    ),
    (
        {"customer": "Sam", "items": [("Milk", 4), ("Ice Cream", 4), ("Cheese", 2)]},
        [
            "Order for Sam:",
            "  - Milk:           4 à 2.50 = 10.00",
            "  - Ice Cream:      4 à 3.50 = 14.00",
            "  - Cheese:         2 à 3.00 = 6.00",
            "Subtotal:        30.00",
            "Volume discount: 3.00",
            "Total:           27.00",
        ],
    ),
    (
        {
            "customer": "Jane's Milky Way",
            "items": [("Cheese", 8), ("Ice Cream", 8), ("Milk", 2)],
        },
        [
            "Order for Jane's Milky Way:",
            "  - Cheese:         8 à 3.00 = 22.80 (discount: 1.20)",
            "  - Ice Cream:      8 à 3.50 = 26.60 (discount: 1.40)",
            "  - Milk:           2 à 2.50 = 5.00",
            "Subtotal:        54.40",
            "Volume discount: 5.44",
            "Total:           48.96",
        ],
    ),
    (
        {
            "customer": "Dave's Emporium",
            "items": [
                ("Hammer", 5),
                ("Nails", 100),
                ("Ladder", 1),
                ("Drill", 5),
                ("Xbox", 2),
                ("TV", 5),
                ("Phone", 8),
            ],
        },
        [
            "Order for Dave's Emporium:",
            "  - Hammer:         5 à   10.00 =   45.00 (discount: 5.00)",
            "  - Nails:        100 à    0.10 =    9.00 (discount: 1.00)",
            "  - Ladder:         1 à  100.00 =  100.00",
            "  - Drill:          5 à    5.00 =   22.50 (discount: 2.50)",
            "  - Xbox:           2 à  250.00 =  500.00",
            "  - TV:             5 à 1000.00 = 4900.00 (discount: 100.00)",
            "  - Phone:          8 à  800.00 = 6272.00 (discount: 128.00)",
            "Subtotal:        11848.50",
            "Volume discount: 251.09",
            "Total:           11597.41",
        ],
    ),
]


def normalize_whitespace(text):
    return [" ".join(line.split()) for line in text]


@pytest.mark.parametrize("order, expected", _test_cases)
def test_generate_invoice(order, expected):
    expected = normalize_whitespace(expected)

    result = generate_invoice(order, _products)

    assert normalize_whitespace(result.split("\n")) == expected
