from decimal import Decimal
from uuid import uuid4

from customer import Customer
from orderItem import OrderItem


class Order:
    """Represent a customer's e-commerce order."""

    def __init__(self, customer: Customer) -> None:

        if not isinstance(customer, Customer):
            raise TypeError(
                "customer must be a Customer object."
            )

        self.order_id = str(uuid4())
        self.customer = customer
        self.items: list[OrderItem] = []
        self.status = "Pending"

    def add_item(self, item: OrderItem) -> None:
        """Add an item to the order."""

        if not isinstance(item, OrderItem):
            raise TypeError(
                "item must be an OrderItem object."
            )

        self.items.append(item)


    def calculate_total(self) -> Decimal:
        """Calculate the total order value."""

        total = Decimal("0.00")

        for item in self.items:
            total += item.calculate_subtotal()

        return total
    
    def checkout(self) -> None:
        """Complete the order and reduce product stock."""

        if not self.items:
            raise ValueError(
                "Cannot checkout an empty order."
            )

        if self.status == "Completed":
            raise ValueError(
                "Order has already been completed."
            )

        for item in self.items:
            item.product.reduce_stock(item.quantity)

        self.status = "Completed"

    def get_summary(self) -> str:
        """Generate a readable order summary."""

        lines = [
            f"Order ID: {self.order_id}",
            f"Customer: {self.customer.name}",
            f"Customer: {self.customer.name}",
            f"Status: {self.status}",
            "",
            "Items:",
        ]

        for item in self.items:
            lines.append(f"  - {item}")

        lines.extend(
            [
                "",
                f"Total: ${self.calculate_total():.2f} NZD",
            ]
        )

        return "\n".join(lines)


    def __str__(self) -> str:
        """Return a readable order representation."""

        return (
            f"Order {self.order_id} | "
            f"{self.customer.name} | "
            f"{self.status}"
        )