def apply_attribute(node: Node, attr: XmlAttr):
    setter = get_setter(attr)
    stripped_value = attr.value.strip() if attr.value else ''
    if is_expression(stripped_value):
        binding_type, expr_body = parse_expression(stripped_value)
        binder().apply(binding_type, node=node, attr=attr, modifier=setter,
            expr_body=expr_body)
    else:
        setter(node, attr.name, attr.value)