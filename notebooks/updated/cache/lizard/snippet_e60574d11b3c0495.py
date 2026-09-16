def is_tag_matched(self, tag, **attribute_filter):
    if len(attribute_filter) <= 0:
        return True
    for attr, value in attribute_filter.items():
        _value = tag.get(self._ns(attr))
        if _value is None:
            log.warning('Failed to get the attribute with namespace')
            _value = tag.get(attr)
        if _value != value:
            return False
    return True