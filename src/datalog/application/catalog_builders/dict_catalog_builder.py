from .base_catalog_builder import BaseCatalogBuilder

class DictCatalogBuilder(BaseCatalogBuilder):

    def build(self, *args, **kwargs):
        return super().build(*args, **kwargs)