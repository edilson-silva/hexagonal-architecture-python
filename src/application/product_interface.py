from abc import ABCMeta, abstractmethod

from application.status_enum import StatusEnum


class ProductInterface(metaclass=ABCMeta):
    @abstractmethod
    def is_valid(self) -> bool:
        """Verify if product is valid"""
        raise NotImplementedError()

    @abstractmethod
    def enable(self) -> None:
        """Enable product"""
        raise NotImplementedError()

    @abstractmethod
    def disable(self) -> None:
        """Disable product"""
        raise NotImplementedError()

    @abstractmethod
    def get_id(self) -> str:
        """Get product id"""
        raise NotImplementedError()

    @abstractmethod
    def get_name(self) -> str:
        """Get product name"""
        raise NotImplementedError()

    @abstractmethod
    def get_status(self) -> StatusEnum:
        """Get product status"""
        raise NotImplementedError()

    @abstractmethod
    def get_price(self) -> float:
        """Get product price"""
        raise NotImplementedError()
