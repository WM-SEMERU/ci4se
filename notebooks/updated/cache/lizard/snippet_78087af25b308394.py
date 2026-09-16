def infer_typing_attr(node, context=None):
    try:
        value = next(node.value.infer())
    except InferenceError as exc:
        raise UseInferenceDefault from exc
    if not value.qname().startswith('typing.'):
        raise UseInferenceDefault
    node = extract_node(TYPING_TYPE_TEMPLATE.format(value.qname().split('.'
        )[-1]))
    return node.infer(context=context)