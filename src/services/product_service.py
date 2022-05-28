from typing import Optional
from src.application.product import Product
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

    def create(self, name: str, price: float) -> Optional[ProductInterface]:
        """Create a product

        Args:
            name (str): Product name
            price (float): Product price

        Returns:
            Optional[ProductInterface]: Created product or None
        """
        try:
            product = Product(name=name, price=price)
            product.is_valid()
            return self.persistence.save(product=product)
        except ValueError:
            return None
