"""
Bank transfer payment implementation.
"""

from decimal import Decimal

from payment import Payment


class BankTransferPayment(Payment):
    """
    Represent a bank transfer payment.

    Implements the abstract Payment interface.
    """

    def __init__(
        self,
        amount: Decimal,
        bank_account: str,
    ) -> None:
        """
        Initialize a bank transfer payment.

        Args:
            amount: Payment amount.
            bank_account: Bank account identifier.
        """

        super().__init__(amount)

        bank_account = bank_account.strip()

        if not bank_account:
            raise ValueError(
                "Bank account cannot be empty."
            )

        self.bank_account = bank_account

    def pay(self) -> str:
        """
        Process the bank transfer.

        Returns:
            Payment result message.
        """

        return (
            f"Bank transfer of "
            f"${self.amount:.2f} NZD "
            f"processed from account "
            f"{self.bank_account}."
        )

    def refund(self) -> str:
        """
        Refund the bank transfer.

        Returns:
            Refund result message.
        """

        return (
            f"${self.amount:.2f} NZD refund "
            f"initiated to bank account "
            f"{self.bank_account}."
        )