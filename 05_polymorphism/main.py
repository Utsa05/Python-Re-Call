"""
Application entry point.
"""

from notification_controller import NotificationController
from email_notification import EmailNotification
from push_notification import PushNotification
from sms_notification import SMSNotification


def main() -> None:
    """Start the notification application."""

    controller = NotificationController()

    try:
        # --------------------------------------------------
        # Create different notification types
        # --------------------------------------------------

        email = EmailNotification(
            recipient="utsa@example.com",
            message="Your order has been shipped.",
        )

        sms = SMSNotification(
            recipient="+64210000000",
            message="Your order will arrive tomorrow.",
        )

        push = PushNotification(
            recipient="user-12345",
            message="You have a new order update.",
        )

        # --------------------------------------------------
        # Add notifications
        # --------------------------------------------------

        controller.add_notification(email)
        controller.add_notification(sms)
        controller.add_notification(push)

        # --------------------------------------------------
        # Send all notifications
        # --------------------------------------------------

        print("=" * 60)
        print("SENDING NOTIFICATIONS")
        print("=" * 60)

        controller.send_all()

    except ValueError as error:
        print("\nERROR:")
        print(f"Invalid notification data: {error}")

    except TypeError as error:
        print("\nERROR:")
        print(f"Invalid notification type: {error}")

    except Exception as error:
        print("\nERROR:")
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()