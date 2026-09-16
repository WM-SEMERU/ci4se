def _handleable_truism(t):
    if len(t.args) < 2:
        l.debug("can't do anything with an unop bool")
    elif t.args[0].cardinality > 1 and t.args[1].cardinality > 1:
        l.debug("can't do anything because we have multiple multivalued guys")
        return False
    else:
        return True