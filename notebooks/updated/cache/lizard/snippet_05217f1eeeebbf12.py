def _stmt_from_rule(model, rule_name, stmts):
    stmt_uuid = None
    for ann in model.annotations:
        if ann.predicate == 'from_indra_statement':
            if ann.subject == rule_name:
                stmt_uuid = ann.object
                break
    if stmt_uuid:
        for stmt in stmts:
            if stmt.uuid == stmt_uuid:
                return stmt