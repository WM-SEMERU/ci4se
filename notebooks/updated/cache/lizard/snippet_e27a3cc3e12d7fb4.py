def normalize_constraints(constraints, flds):
    local_constraints = constraints or []
    local_constraints = [dict(**c) for c in local_constraints]
    local_constraints = [c for c in local_constraints if c.get('field') in
        flds or not c.get('optional')]
    return local_constraints