def infer_dict(node, context=None):
    call = arguments.CallSite.from_call(node)
    if call.has_invalid_arguments() or call.has_invalid_keywords():
        raise UseInferenceDefault
    args = call.positional_arguments
    kwargs = list(call.keyword_arguments.items())
    if not args and not kwargs:
        return nodes.Dict()
    elif kwargs and not args:
        items = [(nodes.Const(key), value) for key, value in kwargs]
    elif len(args) == 1 and kwargs:
        elts = _get_elts(args[0], context)
        keys = [(nodes.Const(key), value) for key, value in kwargs]
        items = elts + keys
    elif len(args) == 1:
        items = _get_elts(args[0], context)
    else:
        raise UseInferenceDefault()
    value = nodes.Dict(col_offset=node.col_offset, lineno=node.lineno,
        parent=node.parent)
    value.postinit(items)
    return value