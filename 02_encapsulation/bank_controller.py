"""
Application controller for the bank account example.
"""

from decimal import Decimal

from bank_account import BankAccount


class BankController:
    """
    Coordinate bank account operations.

    The controller manages the workflow while the
    BankAccount class manages its own internal state.
    """

    def __init__(self) -> None:
        """Initialize the controller."""

        self.account: BankAccount | None = None

    def create_account(
        self,
        account_number: str,
        account_holder: str,
        initial_balance: Decimal = Decimal("0.00"),
    ) -> BankAccount:
        """
        Create a bank account.

        Returns:
            Created BankAccount object.
        """

        self.account = BankAccount(
            account_number=account_number,
            account_holder=account_holder,
            initial_balance=initial_balance,
        )

        return self.account

    def deposit(
        self,
        amount: Decimal,
    ) -> None:
        """
        Deposit money into the current account.

        Raises:
            RuntimeError: If no account exists.
        """

        self._require_account()

        self.account.deposit(amount)

    def withdraw(
        self,
        amount: Decimal,
    ) -> None:
        """
        Withdraw money from the current account.

        Raises:
            RuntimeError: If no account exists.
        """

        self._require_account()

        self.account.withdraw(amount)

    def show_balance(self) -> None:
        """Display the current account balance."""

        self._require_account()

        print(
            f"Current balance: "
            f"${self.account.get_balance():.2f} NZD"
        )

    def show_account(self) -> None:
        """Display the account summary."""

        self._require_account()

        print(self.account.get_account_summary())

    def _require_account(self) -> None:
        """
        Ensure that an account exists.

        Raises:
            RuntimeError: If no account has been created.
        """

        if self.account is None:
            raise RuntimeError(
                "Create an account before performing this operation."
            )