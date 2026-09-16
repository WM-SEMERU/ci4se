def check_rules_dict(rules):
    from qnet.algebra.pattern_matching import Pattern, ProtoExpr
    if hasattr(rules, 'items'):
        items = rules.items()
    else:
        items = rules
    keys = set()
    for key_rule in items:
        try:
            key, rule = key_rule
        except ValueError:
            raise TypeError('rules does not contain (key, rule) tuples')
        if not isinstance(key, str):
            raise TypeError("Key '%s' is not a string" % key)
        if key in keys:
            raise ValueError("Duplicate key '%s'" % key)
        else:
            keys.add(key)
        try:
            pat, replacement = rule
        except TypeError:
            raise TypeError(
                "Rule in '%s' is not a (pattern, replacement) tuple" % key)
        if not isinstance(pat, Pattern):
            raise TypeError("Pattern in '%s' is not a Pattern instance" % key)
        if pat.head is not ProtoExpr:
            raise ValueError("Pattern in '%s' does not match a ProtoExpr" % key
                )
        if not callable(replacement):
            raise ValueError("replacement in '%s' is not callable" % key)
        else:
            arg_names = inspect.signature(replacement).parameters.keys()
            if not arg_names == pat.wc_names:
                raise ValueError(
                    'arguments (%s) of replacement function differ from the wildcard names (%s) in pattern'
                     % (', '.join(sorted(arg_names)), ', '.join(sorted(pat.
                    wc_names))))
    return OrderedDict(rules)