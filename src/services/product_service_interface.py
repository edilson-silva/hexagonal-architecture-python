from abc import ABCMeta, abstractmethod
from typing import Optional

from src.application.product_interface import ProductInterface


class ProductServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def get(self, id: str) -> Optional[ProductInterface]:
        """Get product by ID

        Args:
            id (str): Product ID

        Raises:
            NotImplementedError: If not implemented in subclasses

        Returns:
            Optional[ProductInterface]: Found product or None
        """
        raise NotImplementedError()

    @abstractmethod
    def create(self, name: str, price: float) -> Optional[ProductInterface]:
        """Create a product

        Args:
            name (str): Product name
            price (float): Product price

        Raises:
            NotImplementedError: If not implemented in subclasses

        Returns:
            Optional[ProductInterface]: Created product or None
        """
        raise NotImplementedError()

    @abstractmethod
    def enable(self, product: ProductInterface) -> Optional[ProductInterface]:
        """Enable a product

        Args:
            product (ProductInterface): Product to enable

        Raises:
            NotImplementedError: If not implemented in subclasses

        Returns:
            Optional[ProductInterface]: Enabled product or None
        """
        raise NotImplementedError()

    @abstractmethod
    def disable(self, product: ProductInterface) -> Optional[ProductInterface]:
        """Disable a product

        Args:
            product (ProductInterface): Product to disable

        Raises:
            NotImplementedError: If not implemented in subclasses

        Returns:
            Optional[ProductInterface]: Disabled product or None
        """
        raise NotImplementedError()
