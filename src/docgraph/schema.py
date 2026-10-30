from typing import Literal

from pydantic import BaseModel, Field

EntityType = Literal["Organization", "Facility", "Material", "Product", "Finding", "Document"]
RelType = Literal["SUPPLIES", "OPERATES", "PRODUCES", "USES", "AFFECTS", "FOUND_AT", "PARTY_TO", "REFERENCES"]


class Entity(BaseModel):
    name: str
    type: EntityType
    aliases: list[str] = Field(default_factory=list)


class Edge(BaseModel):
    src: str
    rel: RelType
    dst: str
    doc: str
    page: int
    chunk_id: str  # provenance is mandatory: no default
    conf: float = Field(ge=0, le=1)


class Extraction(BaseModel):
    entities: list[Entity]
    edges: list[Edge]
