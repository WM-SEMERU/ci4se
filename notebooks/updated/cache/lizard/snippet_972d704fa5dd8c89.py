def filter(table, predicates):
    resolved_predicates = _resolve_predicates(table, predicates)
    return _L.apply_filter(table, resolved_predicates)