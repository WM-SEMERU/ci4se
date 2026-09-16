def resolve_calls(func):
    node = quoting.parse_function(func)
    ResolveCalls(func).visit(node)
    return node