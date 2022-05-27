from abc import ABCMeta

from src.services.product_reader_service_interface import ProductReaderServiceInterface
from src.services.product_writer_service_interface import ProductWriterServiceInterface


class ProductPersistenceServiceInterface(
    ProductReaderServiceInterface, ProductWriterServiceInterface, metaclass=ABCMeta
):
    """A product persistence service interface"""

    pass
