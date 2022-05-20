from application.product_interface import ProductInterface
from application.status_enum import StatusEnum


class Product(ProductInterface):
    def is_valid(self) -> bool:
        return False

    def enable(self) -> None:
        if self.price > 0:
            self.status = StatusEnum.ENABLED

        raise ValueError("The price must be greater than zero to enable the product")

    def disable(self) -> None:
        pass

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_status(self) -> str:
        return self.status.value

    def get_price(self) -> float:
        return self.price
