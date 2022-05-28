from math import prod
from unittest.mock import Mock

import pytest
from src.application.product_interface import ProductInterface
from src.services.product_persistence_service_interface import (
    ProductPersistenceServiceInterface,
)
from src.services.product_service import ProductService


@pytest.fixture
def product_mock():
    # Define product mock
    return Mock(spec=ProductInterface, name="product")


@pytest.fixture
def persistence_mock():
    # Defining product persistence service interface mock and setting mocked get method return value
    return Mock(spec=ProductPersistenceServiceInterface, name="persistence")


def test_product_service_get_should_return_a_product(product_mock, persistence_mock):
    persistence_mock.get.return_value = product_mock

    service = ProductService(persistence_mock)
    result = service.get(id="abc")

    assert product_mock == result


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


def test_product_service_disable_should_return_a_product():
    # Define product mock
    product = Mock(spec=ProductInterface, name="product")
    product.disable.return_value = None

    # Defining product persistence service interface mock and setting mocked get method return value
    persistence = Mock(spec=ProductPersistenceServiceInterface, name="persistence")
    persistence.save.return_value = product

    service = ProductService(persistence=persistence)
    result = service.disable(product=product)

    assert product == result
