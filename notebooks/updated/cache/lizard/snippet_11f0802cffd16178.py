def make_processitem_username(username, condition='contains', negate=False,
    preserve_case=False):
    document = 'ProcessItem'
    search = 'ProcessItem/Username'
    content_type = 'string'
    content = username
    ii_node = ioc_api.make_indicatoritem_node(condition, document, search,
        content_type, content, negate=negate, preserve_case=preserve_case)
    return ii_node