def parse_namespace(parser, event, node):
    name = _get_required_attribute(node, 'NAME')
    next_event, next_node = six.next(parser)
    if not _is_end(next_event, next_node, 'NAMESPACE'):
        raise ParseError('Expecting end NAMESPACE')
    return name