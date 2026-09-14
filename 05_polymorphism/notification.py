"""
Base notification model.

Demonstrates polymorphism using an abstract base class.
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Abstract base class for notifications.

    Every notification must implement send().
    """

    def __init__(
        self,
        recipient: str,
        message: str,
    ) -> None:
        """
        Initialize a notification.

        Args:
            recipient: Notification recipient.
            message: Notification message.

        Raises:
            ValueError: If recipient or message is empty.
        """

        recipient = recipient.strip()
        message = message.strip()

        if not recipient:
            raise ValueError(
                "Recipient cannot be empty."
            )

        if not message:
            raise ValueError(
                "Message cannot be empty."
            )

        self.recipient = recipient
        self.message = message

    @abstractmethod
    def send(self) -> str:
        """
        Send the notification.

        Every child class must implement this method.
        """

        raise NotImplementedError