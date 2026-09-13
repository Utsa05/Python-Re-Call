from decimal import Decimal


class Product:
    """Represent a product sold through the e-commerce platform."""

    currency = "NZD"

    def __init__(
        self,
        product_id: str,
        name: str,
        price: Decimal,
        stock: int = 0,
    ) -> None:

        product_id = product_id.strip()
        name = name.strip()

        if not product_id:
            raise ValueError("Product ID cannot be empty.")

        if not name:
            raise ValueError("Product name cannot be empty.")

        if price < Decimal("0"):
            raise ValueError("Product price cannot be negative.")

        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, quantity: int = 1) -> bool:
        """Check whether enough stock is available."""

        if quantity <= 0:
            return False

        return self.stock >= quantity

    def reduce_stock(self, quantity: int) -> None:
        """Reduce inventory after a successful purchase."""

        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero."
            )

        if not self.is_available(quantity):
            raise ValueError(
                f"Insufficient stock for '{self.name}'."
            )

        self.stock -= quantity

    def get_stock(self) -> int:
        """Return current stock."""

        return self.stock

    def __str__(self) -> str:
        """Return a readable product representation."""

        return (
            f"{self.name} | "
            f"${self.price:.2f} {self.currency} | "
            f"Stock: {self.stock}"
        )