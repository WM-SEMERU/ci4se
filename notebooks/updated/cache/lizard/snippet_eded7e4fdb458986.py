def get_causal_edge(stmt, activates):
    any_contact = any(evidence.epistemics.get('direct', False) for evidence in
        stmt.evidence)
    if any_contact:
        return pc.DIRECTLY_INCREASES if activates else pc.DIRECTLY_DECREASES
    return pc.INCREASES if activates else pc.DECREASES