import pytest

from datalog.domain.dependency_graph import DependencyGraph

def test_generate_dependency_graph(table_map):
    dg = DependencyGraph(table_map)
    dg.generate()