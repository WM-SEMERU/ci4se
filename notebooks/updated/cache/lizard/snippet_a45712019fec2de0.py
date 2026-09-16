def _remove_unit_rule(g, rule):
    new_rules = [x for x in g.rules if x != rule]
    refs = [x for x in g.rules if x.lhs == rule.rhs[0]]
    new_rules += [build_unit_skiprule(rule, ref) for ref in refs]
    return Grammar(new_rules)