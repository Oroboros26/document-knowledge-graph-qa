import pytest

from docgraph.cypher_guard import validate


def test_read_query_passes():
    q = "MATCH (f)-[:AFFECTS]->(m) RETURN m.name"
    assert validate(q) == q


@pytest.mark.parametrize("q", ["MATCH (n) DETACH DELETE n", "MATCH (a)-[:HACKS]->(b) RETURN b"])
def test_unsafe_rejected(q):
    with pytest.raises(ValueError):
        validate(q)
