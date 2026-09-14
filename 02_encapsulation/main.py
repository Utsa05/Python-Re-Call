"""
Application entry point.
"""

from decimal import Decimal

from bank_controller import BankController


def main() -> None:
    """Start the bank account application."""

    controller = BankController()

    try:
        # -----------------------------------------------
        # 1. Create account
        # -----------------------------------------------

        controller.create_account(
            account_number="NZ-10001",
            account_holder="Utsa Chandra",
            initial_balance=Decimal("1000.00"),
        )

        print("=" * 60)
        print("ACCOUNT CREATED")
        print("=" * 60)

        controller.show_account()

        # -----------------------------------------------
        # 2. Deposit money
        # -----------------------------------------------

        print("\n" + "=" * 60)
        print("DEPOSIT")
        print("=" * 60)

        controller.deposit(
            Decimal("500.00")
        )

        controller.show_balance()

        # -----------------------------------------------
        # 3. Withdraw money
        # -----------------------------------------------

        print("\n" + "=" * 60)
        print("WITHDRAWAL")
        print("=" * 60)

        controller.withdraw(
            Decimal("250.00")
        )

        controller.show_balance()

        # -----------------------------------------------
        # 4. Final account
        # -----------------------------------------------

        print("\n" + "=" * 60)
        print("FINAL ACCOUNT")
        print("=" * 60)

        controller.show_account()

    except ValueError as error:
        print("\nERROR:")
        print(f"Transaction failed: {error}")

    except RuntimeError as error:
        print("\nERROR:")
        print(f"Application error: {error}")

    except Exception as error:
        print("\nERROR:")
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()