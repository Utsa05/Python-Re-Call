from decimal import Decimal

from customer import Customer
from order import Order
from orderItem import OrderItem
from product import Product


class ECommerceController:
    """
    Coordinate the e-commerce application workflow.

    The controller connects the different domain objects
    and controls the order in which operations happen.
    """
    def __init__(self) -> None:
        self.customer: Customer | None = None
        self.products: list[Product] = []
        self.order: Order | None = None

    def create_customer(
        self,
        name: str,
        email: str,
        phone_no: str,
        address: str
    ) -> Customer:

        self.customer = Customer(
            name=name,
            email=email,
            phone_no=phone_no,
            address=address
        )

        return self.customer

    def add_product(
        self,
        product_id: str,
        name: str,
        price: Decimal,
        stock: int,
    ) -> Product:

        product = Product(
            product_id=product_id,
            name=name,
            price=price,
            stock=stock,
        )

        self.products.append(product)

        return product

    def create_order(self) -> Order:

        if self.customer is None:
            raise RuntimeError(
                "Create a customer before creating an order."
            )

        self.order = Order(
            customer=self.customer
        )

        return self.order

    def add_product_to_order(
        self,
        product: Product,
        quantity: int = 1,
    ) -> OrderItem:

        if self.order is None:
            raise RuntimeError(
                "Create an order before adding products."
            )

        item = OrderItem(
            product=product,
            quantity=quantity,
        )

        self.order.add_item(item)

        return item

    def checkout(self) -> None:

        if self.order is None:
            raise RuntimeError(
                "Create an order before checkout."
            )

        self.order.checkout()

    def get_order_total(self) -> Decimal:

        if self.order is None:
            raise RuntimeError(
                "No active order exists."
            )

        return self.order.calculate_total()

    def show_order(self) -> None:

        if self.order is None:
            print("No active order.")
            return

        print(self.order.get_summary())

    def show_products(self) -> None:

        if not self.products:
            print("No products available.")
            return

        for product in self.products:
            print(product)