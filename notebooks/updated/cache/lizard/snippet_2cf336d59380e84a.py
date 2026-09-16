def parse_host(parser, event, node):
    host = ''
    next_event, next_node = six.next(parser)
    if next_event == pulldom.CHARACTERS:
        host = next_node.nodeValue
        next_event, next_node = six.next(parser)
    if not _is_end(next_event, next_node, 'HOST'):
        raise ParseError('Expecting end HOST')
    return host