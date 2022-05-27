from abc import ABCMeta, abstractmethod
from typing import Optional

from src.application.product_interface import ProductInterface


class ProductWriterServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def save(self, product: ProductInterface) -> Optional[ProductInterface]:
        """Save product

        Args:
            product (ProductInterface): Product to save

        Raises:
            NotImplementedError: If function not implemented in subclasses

        Returns:
            Optional[ProductInterface]: Saved product or None
        """
        raise NotImplementedError()
