from src.application.product_interface import ProductInterface
from src.application.status_enum import StatusEnum
from uuid import UUID, uuid4


class Product(ProductInterface):
    def __init__(
        self, name: str, price: float = 0, status: str = StatusEnum.DISABLED
    ) -> None:
        self.__id = uuid4()
        self.__name = name
        self.__price = price
        self.__status = StatusEnum(status)

    def is_valid(self) -> bool:
        if not self.__status:
            raise ValueError(
                f"The status must be one of the following: {', '.join(StatusEnum.get_members_values())}"
            )

        if (
            not isinstance(self.__price, float) and not isinstance(self.__price, int)
        ) or self.__price < 0:
            raise ValueError("The price must be greater or equal zero")

        if not isinstance(self.__id, UUID):
            raise ValueError("The ID must be an UUID")

        if not isinstance(self.__name, str) or (
            isinstance(self.__name, str) and not self.__name
        ):
            raise ValueError("The Name must be string and is required")

        return True

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

    def get_id(self) -> UUID:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    def get_status(self) -> str:
        return self.__status

    def get_price(self) -> float:
        return self.__price
