"""
Credit card payment implementation.
"""

from decimal import Decimal

from payment import Payment


class CreditCardPayment(Payment):
    """
    Represent a credit card payment.

    Implements the abstract Payment interface.
    """

    def __init__(
        self,
        amount: Decimal,
        card_last_four: str,
    ) -> None:
        """
        Initialize a credit card payment.

        Args:
            amount: Payment amount.
            card_last_four: Last four digits of the card.
        """

        super().__init__(amount)

        card_last_four = card_last_four.strip()

        if len(card_last_four) != 4:
            raise ValueError(
                "Card number must contain exactly four digits."
            )

        if not card_last_four.isdigit():
            raise ValueError(
                "Card number must contain digits only."
            )

        self.card_last_four = card_last_four

    def pay(self) -> str:
        """
        Process the credit card payment.

        Returns:
            Payment result message.
        """

        return (
            f"Credit card ending in "
            f"****{self.card_last_four} "
            f"charged ${self.amount:.2f} NZD."
        )

    def refund(self) -> str:
        """
        Refund the credit card payment.

        Returns:
            Refund result message.
        """

        return (
            f"${self.amount:.2f} NZD refunded "
            f"to card ending in ****{self.card_last_four}."
        )