from typing import Optional
from src.application.product_interface import ProductInterface
from src.services.product_persistence_service_interface import (
    ProductPersistenceServiceInterface,
)


class ProductService:
    def __init__(self, persistence: ProductPersistenceServiceInterface) -> None:
        self.persistence = persistence

    def get(self, id: str) -> Optional[ProductInterface]:
        """Get product by ID

        Args:
            id (str): Product ID

        Returns:
            Optional[ProductInterface]: Found product or None
        """
        return self.persistence.get(id)
