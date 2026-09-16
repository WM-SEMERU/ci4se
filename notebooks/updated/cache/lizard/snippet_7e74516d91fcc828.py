def _remove_xml(xast, node, context, if_empty=False):
    if isinstance(xast, ast.Step):
        if isinstance(xast.node_test, ast.NameTest):
            if xast.axis in (None, 'child'):
                return _remove_child_node(node, context, xast, if_empty=
                    if_empty)
            elif xast.axis in ('@', 'attribute'):
                return _remove_attribute_node(node, context, xast)
        elif _is_text_nodetest(xast):
            node.text = ''
            return True
    elif isinstance(xast, ast.BinaryExpression):
        if xast.op == '/':
            left_xpath = serialize(xast.left)
            left_node = _find_xml_node(left_xpath, node, context)
            if left_node is not None:
                removed = _remove_xml(xast.right, left_node, context,
                    if_empty=if_empty)
                if removed and _predicate_is_constructible(left_xpath):
                    _remove_xml(xast.left, node, context, if_empty=True)
                return removed
    return False