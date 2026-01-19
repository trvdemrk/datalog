from abc import ABC, abstractmethod
from ..catalog import Catalog

class BaseCatalogBuilder(ABC):

    @abstractmethod
    def build(self, *args, **kwargs) -> Catalog:
        raise NotImplementedError("build not currently implemented for relevant CatalogBuilder")