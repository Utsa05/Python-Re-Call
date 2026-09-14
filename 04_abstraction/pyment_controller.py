"""
Application controller for the payment system.
"""

from payment import Payment


class PaymentController:
    """
    Coordinate payment operations.

    The controller works with the abstract Payment type
    instead of depending on one specific payment method.
    """

    def __init__(self) -> None:
        """Initialize the payment controller."""

        self.payment: Payment | None = None

    def set_payment(
        self,
        payment: Payment,
    ) -> None:
        """
        Set the current payment method.

        Args:
            payment: A concrete Payment implementation.

        Raises:
            TypeError: If the object is not a Payment.
        """

        if not isinstance(payment, Payment):
            raise TypeError(
                "payment must be a Payment object."
            )

        self.payment = payment

    def process_payment(self) -> None:
        """
        Process the current payment.
        """

        self._require_payment()

        print(self.payment.pay())

    def process_refund(self) -> None:
        """
        Process a refund for the current payment.
        """

        self._require_payment()

        print(self.payment.refund())

    def show_amount(self) -> None:
        """Display the payment amount."""

        self._require_payment()

        print(
            f"Payment amount: "
            f"${self.payment.get_amount():.2f} NZD"
        )

    def _require_payment(self) -> None:
        """
        Ensure that a payment exists.

        Raises:
            RuntimeError: If no payment has been selected.
        """

        if self.payment is None:
            raise RuntimeError(
                "Set a payment before performing this operation."
            )