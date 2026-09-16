def set_attribute(token_or_hostname, **kwargs):
    node = nago.core.get_node(token_or_hostname) or {}
    if not kwargs:
        return 'No changes made'
    for k, v in kwargs.items():
        node[k] = v
    node.save()
    return 'Saved %s changes' % len(kwargs)