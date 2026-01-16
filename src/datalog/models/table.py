from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Optional

TABLE_ID_FIELDS = frozenset(['name', 'columns', 'description'])

@dataclass(slots=True, frozen=True)
class TableId:
    """Identifier class to be used for uniquely identifying tables"""
    # Subject to change, hopefully make it frozen one day
    name : str
    schema : str

@dataclass(slots=True)
class Table:
    """A table entity representing relevant metadata of a database Table"""
    # Creating an id that uniquely identifies a Table
    id : TableId
    # Instance variables (What defines a table object?)
    name : str
    schema : str
    columns : set
    description : Optional[str] = None
    load_sql : Optional[str] = None
    direct_ancestors : Optional[set[TableId]] = None

    # A string representation used for universal searching
    _search_expr : Optional[str] = None

    @property
    def search_expr(self):
        if not self._search_expr:
            self._search_expr = ' '.join([f"{field}:{getattr(self, field)}" for field in TABLE_ID_FIELDS])
        return self._search_expr

    @classmethod
    def from_dict(cls, metadata : dict):
        pass