def _rules_attr(cls):
    from qnet.algebra.core.algebraic_properties import match_replace, match_replace_binary
    if match_replace in cls.simplifications:
        return '_rules'
    elif match_replace_binary in cls.simplifications:
        return '_binary_rules'
    else:
        raise TypeError(
            'class %s does not have match_replace or match_replace_binary in its simplifications'
             % cls.__name__)