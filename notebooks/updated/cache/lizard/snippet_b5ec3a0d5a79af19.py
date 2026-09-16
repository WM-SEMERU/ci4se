def lookup(var_name, contexts=(), start=0):
    start = len(contexts) if start >= 0 else start
    for context in reversed(contexts[:start]):
        try:
            if var_name in context:
                return context[var_name]
        except TypeError as te:
            continue
    return None