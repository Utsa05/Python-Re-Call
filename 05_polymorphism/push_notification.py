"""
Push notification implementation.
"""

from notification import Notification


class PushNotification(Notification):
    """
    Represent a push notification.
    """

    def send(self) -> str:
        """
        Send a push notification.

        Returns:
            Result of the push notification operation.
        """

        return (
            f"Push notification sent to {self.recipient}: "
            f"{self.message}"
        )