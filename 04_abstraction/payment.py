"""
Abstract payment system.

Demonstrates abstraction using Python's ABC module.
"""

from abc import ABC, abstractmethod
from decimal import Decimal


class Payment(ABC):
    """
    Abstract base class for payment methods.

    Payment defines what every payment method MUST do,
    but does not define exactly HOW each method does it.
    """

    def __init__(
        self,
        amount: Decimal,
    ) -> None:
        """
        Initialize a payment.

        Args:
            amount: Payment amount.

        Raises:
            ValueError: If the amount is invalid.
        """

        if amount <= Decimal("0.00"):
            raise ValueError(
                "Payment amount must be greater than zero."
            )

        self.amount = amount

    @abstractmethod
    def pay(self) -> str:
        """
        Process the payment.

        Every child payment class must implement this method.
        """

        raise NotImplementedError

    @abstractmethod
    def refund(self) -> str:
        """
        Refund the payment.

        Every child payment class must implement this method.
        """

        raise NotImplementedError

    def get_amount(self) -> Decimal:
        """
        Return the payment amount.

        Returns:
            Payment amount.
        """

        return self.amount