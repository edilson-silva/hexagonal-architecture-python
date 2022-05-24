from src.application.product_interface import ProductInterface
from src.application.status_enum import StatusEnum


class Product(ProductInterface):
    def __init__(
        self, id: int, name: str, price: float = 0, status: str = StatusEnum.INVALID
    ) -> None:
        self.__id = id
        self.__name = name
        self.__price = price
        self.__status = StatusEnum(status)

    def is_valid(self) -> bool:
        if not self.__status:
            raise ValueError(
                f"The status must be one of the following: {', '.joint(StatusEnum.get_members_values())}"
            )
        return False

    def enable(self) -> None:
        if self.__price <= 0:
            raise ValueError(
                "The price must be greater than zero to enable the product"
            )

        self.__status = StatusEnum.ENABLED

    def disable(self) -> None:
        if self.__price != 0:
            raise ValueError("The price must be zero to disable the product")

        self.__status = StatusEnum.DISABLED

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_status(self) -> str:
        return self.__status

    def get_price(self) -> float:
        return self.__price
