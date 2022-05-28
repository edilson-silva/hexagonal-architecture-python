from math import prod
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


def test_product_service_create_should_return_a_product():
    # Define product mock
    product = Mock(spec=ProductInterface, name="product")

    # Defining product persistence service interface mock and setting mocked get method return value
    persistence = Mock(spec=ProductPersistenceServiceInterface, name="persistence")
    persistence.save.return_value = product

    service = ProductService(persistence=persistence)
    result = service.create(name="Product 1", price=10)

    assert product == result


def test_product_service_enable_should_return_a_product():
    # Define product mock
    product = Mock(spec=ProductInterface, name="product")
    product.enable.return_value = None

    # Defining product persistence service interface mock and setting mocked get method return value
    persistence = Mock(spec=ProductPersistenceServiceInterface, name="persistence")
    persistence.save.return_value = product

    service = ProductService(persistence=persistence)
    result = service.enable(product=product)

    assert product == result
