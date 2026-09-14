"""
SMS notification implementation.
"""

from notification import Notification


class SMSNotification(Notification):
    """
    Represent an SMS notification.
    """

    def send(self) -> str:
        """
        Send an SMS notification.

        Returns:
            Result of the SMS operation.
        """

        return (
            f"SMS sent to {self.recipient}: "
            f"{self.message}"
        )