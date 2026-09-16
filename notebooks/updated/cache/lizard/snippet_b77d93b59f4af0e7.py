def parse_instancepath(parser, event, node):
    next_event, next_node = six.next(parser)
    if not _is_start(next_event, next_node, 'NAMESPACEPATH'):
        raise ParseError('Expecting NAMESPACEPATH')
    host, namespacepath = parse_namespacepath(parser, next_event, next_node)
    next_event, next_node = six.next(parser)
    if not _is_start(next_event, next_node, 'INSTANCENAME'):
        print(next_event, next_node)
        raise ParseError('Expecting INSTANCENAME')
    instancename = parse_instancename(parser, next_event, next_node)
    instancename.host = host
    instancename.namespace = namespacepath
    return instancename