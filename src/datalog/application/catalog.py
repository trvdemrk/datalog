from typing import Dict, List, Iterable
from ..models.table import Table, TableId
import re

class Catalog(object):
    """"""

    def __init__(self, tables : Dict[TableId, Table]):
        self._tables : Dict[TableId, Table] = tables
    
    def search(self, term : str):
        """
        Specifically searches based on possible filters
        
        :param self: An instance of the Catalog class
        :param regex: Description
        :type regex: str
        """
        pattern = re.compile(f'.*{term}.*')

        results = []
        for table in self._tables.values():
            if pattern.search(table.search_expr):
                results.append(table)

        return results
        
    def save(self):
        pass
    
    @classmethod
    def build_from_dict(cls, table_metadata_mapping : Dict):
        for table, metadata in table_metadata_mapping:
            pass