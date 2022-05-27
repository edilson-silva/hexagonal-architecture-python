from unittest.mock import Mock
from src.application.product_interface import ProductInterface
from src.services.product_persistence_service_interface import (
    ProductPersistenceServiceInterface,
)
from src.services.product_service import ProductService


def test_product_service_get_should_return_a_product():
    # Define product mock
    product = Mock(spec=ProductInterface, name="product")

    # Defining product persistence service interface mock and setting mocked get method return value
    persistence = Mock(spec=ProductPersistenceServiceInterface, name="persistence")
    persistence.get.return_value = product

    service = ProductService(persistence=persistence)
    result = service.get(id="abc")

    assert product == result
