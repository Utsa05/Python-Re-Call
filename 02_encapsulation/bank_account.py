"""
Bank account domain model.

This module demonstrates encapsulation using a real-world
bank account example.
"""

from decimal import Decimal


class BankAccount:
    """
    Represent a bank account.

    Encapsulation is used to protect the account balance.
    The balance should not be changed directly from outside
    the class.
    """

    bank_name = "NZ Bank"

    def __init__(
        self,
        account_number: str,
        account_holder: str,
        initial_balance: Decimal = Decimal("0.00"),
    ) -> None:
        """
        Initialize a bank account.

        Args:
            account_number: Unique account number.
            account_holder: Name of the account owner.
            initial_balance: Starting account balance.

        Raises:
            ValueError: If account information is invalid.
        """

        account_number = account_number.strip()
        account_holder = account_holder.strip()

        if not account_number:
            raise ValueError(
                "Account number cannot be empty."
            )

        if not account_holder:
            raise ValueError(
                "Account holder name cannot be empty."
            )

        if initial_balance < Decimal("0.00"):
            raise ValueError(
                "Initial balance cannot be negative."
            )

        self.account_number = account_number
        self.account_holder = account_holder

        # Protected attribute.
        # External code should not modify this directly.
        self._balance = initial_balance

    def get_balance(self) -> Decimal:
        """
        Return the current account balance.

        Returns:
            Current balance.
        """

        return self._balance

    def deposit(
        self,
        amount: Decimal,
    ) -> None:
        """
        Deposit money into the account.

        Args:
            amount: Amount of money to deposit.

        Raises:
            ValueError: If the amount is invalid.
        """

        if amount <= Decimal("0.00"):
            raise ValueError(
                "Deposit amount must be greater than zero."
            )

        self._balance += amount

    def withdraw(
        self,
        amount: Decimal,
    ) -> None:
        """
        Withdraw money from the account.

        Args:
            amount: Amount of money to withdraw.

        Raises:
            ValueError: If the amount is invalid or
                there are insufficient funds.
        """

        if amount <= Decimal("0.00"):
            raise ValueError(
                "Withdrawal amount must be greater than zero."
            )

        if amount > self._balance:
            raise ValueError(
                "Insufficient funds."
            )

        self._balance -= amount

    def get_account_summary(self) -> str:
        """
        Return account information.

        Returns:
            Formatted account summary.
        """

        return (
            f"Account: {self.account_number}\n"
            f"Holder: {self.account_holder}\n"
            f"Balance: ${self._balance:.2f} NZD"
        )

    def __str__(self) -> str:
        """Return a readable account representation."""

        return (
            f"{self.account_holder} | "
            f"Account: {self.account_number} | "
            f"Balance: ${self._balance:.2f} NZD"
        )