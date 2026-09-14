"""
Application controller for the notification system.
"""

from notification import Notification


class NotificationController:
    """
    Coordinate notification operations.
    """

    def __init__(self) -> None:
        """Initialize the notification controller."""

        self.notifications: list[Notification] = []

    def add_notification(
        self,
        notification: Notification,
    ) -> None:
        """
        Add a notification to the queue.

        Args:
            notification: Notification object.

        Raises:
            TypeError: If the object is not a Notification.
        """

        if not isinstance(notification, Notification):
            raise TypeError(
                "notification must be a Notification object."
            )

        self.notifications.append(notification)

    def send_all(self) -> None:
        """
        Send all notifications.

        Polymorphism happens here.

        The controller does not need to know whether
        the notification is email, SMS, or push.
        """

        if not self.notifications:
            print("No notifications to send.")
            return

        for notification in self.notifications:
            print(notification.send())