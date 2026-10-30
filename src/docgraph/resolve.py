import re

from docgraph.schema import Entity

_SUFFIX = re.compile(r"\b(ag|gmbh|s\.r\.o\.|inc|ltd)\b\.?", re.IGNORECASE)


def normalise(name: str) -> str:
    return re.sub(r"\s+", " ", _SUFFIX.sub("", name.lower())).strip()


def merge(entities: list[Entity]) -> list[Entity]:
    """Merge same-type entities with equal normalised name or alias; keep all names as aliases.
    Limitation: exact-match only, add embedding similarity + LLM tie-break for fuzzy cases ('KT')."""
    out: dict[tuple[str, str], Entity] = {}
    alias_index: dict[tuple[str, str], tuple[str, str]] = {}
    for e in entities:
        keys = {(e.type, normalise(n)) for n in [e.name, *e.aliases]}
        hit = next((alias_index[k] for k in keys if k in alias_index), None)
        key = hit or (e.type, normalise(e.name))
        if key in out:
            cur = out[key]
            cur.aliases = sorted(set(cur.aliases) | set(e.aliases) | ({e.name} - {cur.name}))
        else:
            out[key] = e.model_copy()
        for k in keys:
            alias_index[k] = key
    return list(out.values())
