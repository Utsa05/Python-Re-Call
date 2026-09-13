from decimal import Decimal

from product import Product

class OrderItem:
    """Represent one product line in an order."""

    def __init__(
        self,
        product: Product,
        quantity: int = 1,
    ) -> None:

        if not isinstance(product, Product):
            raise TypeError(
                "product must be a Product object."
            )

        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero."
            )

        if not product.is_available(quantity):
            raise ValueError(
                f"Insufficient stock for '{product.name}'."
            )

        self.product = product
        self.quantity = quantity


def calculate_subtotal(self) -> Decimal:
    """Calculate product price × quantity."""

    return self.product.price * self.quantity

    def __str__(self) -> str:
        """Return a readable order item."""

        return (
            f"{self.product.name} x {self.quantity} "
            f"= ${self.calculate_subtotal():.2f}"
        )