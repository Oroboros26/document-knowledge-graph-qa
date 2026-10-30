import re
from typing import get_args

from docgraph.schema import RelType

WRITE_WORDS = re.compile(r"\b(CREATE|MERGE|DELETE|DETACH|SET|REMOVE|DROP|LOAD|CALL)\b", re.IGNORECASE)
ALLOWED_RELS = set(get_args(RelType)) | {"MENTIONED_IN"}


def validate(cypher: str) -> str:
    """Return the query if safe, else raise ValueError. EXPLAIN against Neo4j is a second gate (not here)."""
    if WRITE_WORDS.search(cypher):
        raise ValueError("write or procedure keyword not allowed")
    unknown = set(re.findall(r"\[:(\w+)", cypher)) - ALLOWED_RELS
    if unknown:
        raise ValueError(f"unknown relation(s): {sorted(unknown)}")
    return cypher
