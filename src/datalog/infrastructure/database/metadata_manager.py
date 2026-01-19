from sqlalchemy.engine import Engine
from sqlalchemy import inspect

class MetadataManager():

    def __init__(self, engine : Engine):
        self._engine = engine

    def retrieve_table_metadata(self):
        insp = inspect(self._engine)

        insp.get_schema_names()
        insp.get_table_names(schema="public")
        insp.get_columns("my_table", schema="public")
        insp.get_pk_constraint("my_table")
        insp.get_foreign_keys("my_table")
        insp.get_indexes("my_table")