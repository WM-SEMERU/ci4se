def _infer_map(node, context):
    values = {}
    for name, value in node.items:
        if isinstance(name, nodes.DictUnpack):
            double_starred = helpers.safe_infer(value, context)
            if not double_starred:
                raise exceptions.InferenceError
            if not isinstance(double_starred, nodes.Dict):
                raise exceptions.InferenceError(node=node, context=context)
            unpack_items = _infer_map(double_starred, context)
            values = _update_with_replacement(values, unpack_items)
        else:
            key = helpers.safe_infer(name, context=context)
            value = helpers.safe_infer(value, context=context)
            if any(not elem for elem in (key, value)):
                raise exceptions.InferenceError(node=node, context=context)
            values = _update_with_replacement(values, {key: value})
    return values