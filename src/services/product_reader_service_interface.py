from abc import ABCMeta, abstractmethod

from typing import Optional

from src.application.product_interface import ProductInterface


class ProductReaderServiceInterface(metaclass=ABCMeta):
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
