from docgraph.resolve import merge
from docgraph.schema import Entity


def test_merge_by_alias_and_suffix():
    ents = [
        Entity(name="Kestrel Textiles s.r.o.", type="Organization", aliases=["Kestrel"]),
        Entity(name="Kestrel", type="Organization"),
        Entity(name="Brno Plant", type="Facility"),
    ]
    out = merge(ents)
    assert len(out) == 2


def test_site_not_merged_with_company():
    ents = [Entity(name="Kestrel", type="Organization"), Entity(name="Kestrel", type="Facility")]
    assert len(merge(ents)) == 2
