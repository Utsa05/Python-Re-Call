"""
Application entry point.
"""

from decimal import Decimal

from bank_transfer_payment import BankTransferPayment
from pyment_controller import PaymentController
from credit_card_payment import CreditCardPayment


def main() -> None:
    """Start the payment application."""

    controller = PaymentController()

    try:
        # --------------------------------------------------
        # Credit card payment
        # --------------------------------------------------

        credit_card = CreditCardPayment(
            amount=Decimal("250.00"),
            card_last_four="1234",
        )

        controller.set_payment(credit_card)

        print("=" * 60)
        print("CREDIT CARD PAYMENT")
        print("=" * 60)

        controller.show_amount()
        controller.process_payment()

        print("\n" + "=" * 60)
        print("CREDIT CARD REFUND")
        print("=" * 60)

        controller.process_refund()

        # --------------------------------------------------
        # Bank transfer payment
        # --------------------------------------------------

        bank_transfer = BankTransferPayment(
            amount=Decimal("500.00"),
            bank_account="NZ123456789",
        )

        controller.set_payment(bank_transfer)

        print("\n" + "=" * 60)
        print("BANK TRANSFER PAYMENT")
        print("=" * 60)

        controller.show_amount()
        controller.process_payment()

        print("\n" + "=" * 60)
        print("BANK TRANSFER REFUND")
        print("=" * 60)

        controller.process_refund()

    except ValueError as error:
        print("\nERROR:")
        print(f"Invalid payment data: {error}")

    except TypeError as error:
        print("\nERROR:")
        print(f"Invalid payment type: {error}")

    except RuntimeError as error:
        print("\nERROR:")
        print(f"Application error: {error}")

    except Exception as error:
        print("\nERROR:")
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()