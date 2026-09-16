def a_list(label=None, kwargs=None, attributes=None):
    result = ['label=%s' % quote(label)] if label is not None else []
    if kwargs:
        items = [('%s=%s' % (quote(k), quote(v))) for k, v in tools.
            mapping_items(kwargs) if v is not None]
        result.extend(items)
    if attributes:
        if hasattr(attributes, 'items'):
            attributes = tools.mapping_items(attributes)
        items = [('%s=%s' % (quote(k), quote(v))) for k, v in attributes if
            v is not None]
        result.extend(items)
    return ' '.join(result)