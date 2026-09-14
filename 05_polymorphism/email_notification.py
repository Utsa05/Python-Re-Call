"""
Email notification implementation.
"""

from notification import Notification


class EmailNotification(Notification):
    """
    Represent an email notification.
    """

    def send(self) -> str:
        """
        Send an email notification.

        Returns:
            Result of the email operation.
        """

        return (
            f"Email sent to {self.recipient}: "
            f"{self.message}"
        )