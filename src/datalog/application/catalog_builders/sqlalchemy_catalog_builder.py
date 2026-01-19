from .base_catalog_builder import BaseCatalogBuilder

class SqlAlchemyCatalogBuilder(BaseCatalogBuilder):
    
    def build(self, *args, **kwargs):
        return super().build(*args, **kwargs)