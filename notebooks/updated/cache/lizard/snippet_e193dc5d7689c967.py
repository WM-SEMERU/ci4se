def complete_rules(rules, cmd):
    if not isinstance(rules, list):
        rules = [rules]
    ret = []
    for r in rules:
        ret += complete_rule(r, cmd)
    return ret