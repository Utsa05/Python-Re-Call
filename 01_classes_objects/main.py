"""
Application entry point.
"""

from decimal import Decimal

from controller import ECommerceController


def main() -> None:
    """Start the e-commerce application."""

    controller = ECommerceController()

    try:
        # --------------------------------------------------
        # 1. Create customer
        # --------------------------------------------------

        controller.create_customer(
            name="Utsa Chandra",
            email="utsa@example.com",
            phone_no="00273375074",
            address="Christurch, New Zealand",
            
        )

        # --------------------------------------------------
        # 2. Create products
        # --------------------------------------------------

        laptop = controller.add_product(
            product_id="PROD-001",
            name="MacBook Air",
            price=Decimal("1699.00"),
            stock=10,
        )

        mouse = controller.add_product(
            product_id="PROD-002",
            name="Wireless Mouse",
            price=Decimal("49.90"),
            stock=25,
        )

        keyboard = controller.add_product(
            product_id="PROD-003",
            name="Mechanical Keyboard",
            price=Decimal("129.00"),
            stock=15,
        )

        # --------------------------------------------------
        # 3. Display products
        # --------------------------------------------------

        print("=" * 60)
        print("PRODUCTS")
        print("=" * 60)

        controller.show_products()

        # --------------------------------------------------
        # 4. Create order
        # --------------------------------------------------

        controller.create_order()

        # --------------------------------------------------
        # 5. Add products to order
        # --------------------------------------------------

        controller.add_product_to_order(
            product=laptop,
            quantity=1,
        )

        controller.add_product_to_order(
            product=mouse,
            quantity=2,
        )

        controller.add_product_to_order(
            product=keyboard,
            quantity=1,
        )

        # --------------------------------------------------
        # 6. Display order total
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("ORDER")
        print("=" * 60)

        print(
            f"Total: "
            f"${controller.get_order_total():.2f} NZD"
        )

        # --------------------------------------------------
        # 7. Display order
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("ORDER SUMMARY")
        print("=" * 60)

        controller.show_order()

        # --------------------------------------------------
        # 8. Checkout
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("CHECKOUT")
        print("=" * 60)

        controller.checkout()

        print("Order completed successfully.")

        # --------------------------------------------------
        # 9. Final order
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("FINAL ORDER")
        print("=" * 60)

        controller.show_order()

        # --------------------------------------------------
        # 10. Updated inventory
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("UPDATED INVENTORY")
        print("=" * 60)

        controller.show_products()

    except ValueError as error:
        print("\nERROR:")
        print(f"Invalid data: {error}")

    except TypeError as error:
        print("\nERROR:")
        print(f"Invalid type: {error}")

    except RuntimeError as error:
        print("\nERROR:")
        print(f"Application error: {error}")

    except Exception as error:
        print("\nERROR:")
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()