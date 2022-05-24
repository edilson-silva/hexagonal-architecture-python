from unittest import TestCase

import pytest

from src.application.product import Product
from src.application.status_enum import StatusEnum


class ProductTest(TestCase):
    def test_product_should_be_enabled_with_price_greater_than_zero(self):
        product = Product(id=1, name="Acer VX5", price=10)
        product.enable()

    def test_product_should_be_enabled_with_price_greater_than_zero_and_status_should_be_enabled(
        self,
    ):
        product = Product(id=1, name="Acer VX5", price=10)
        product.enable()
        assert product.get_status() == StatusEnum.ENABLED

    def test_product_should_be_not_enabled_with_price_equal_to_zero_and_raise_a_value_error_exception(
        self,
    ):
        with pytest.raises(
            ValueError,
            match="The price must be greater than zero to enable the product",
        ):
            product = Product(id=1, name="Acer VX5")
            product.enable()

    def test_product_should_be_desabled_with_price_equal_to_zero(self):
        product = Product(id=2, name="USB C Cable", price=0)
        product.disable()

    def test_product_should_be_disabled_with_price_equal_to_zero_and_status_should_be_disabled(
        self,
    ):
        product = Product(id=2, name="USB C Cable", price=0)
        product.disable()
        assert product.get_status() == StatusEnum.DISABLED

    def test_product_should_be_not_disabled_with_price_greater_than_zero_and_raise_a_value_error_exception(
        self,
    ):
        with pytest.raises(
            ValueError,
            match="The price must be zero to disable the product",
        ):
            product = Product(id=2, name="USB C Cable", price=10)
            product.disable()

    def test_product_with_invalid_status_should_raise_a_value_error_exception(
        self,
    ):
        with pytest.raises(
            ValueError,
            match=f"The status must be one of the following: {', '.join(StatusEnum.get_members_values())}",
        ):
            product = Product(id=3, name="OTG Adapter", status="xpto")
            product.is_valid()

    def test_product_with_invalid_status_should_raise_a_value_error_exception(
        self,
    ):
        with pytest.raises(
            ValueError,
            match=f"The status must be one of the following: {', '.join(StatusEnum.get_members_values())}",
        ):
            product = Product(id=3, name="OTG Adapter", status="xpto")
            product.is_valid()
