def _get_requested_filters(self, **kwargs):
    filters_map = kwargs.get('filters_map') or self.view.get_request_feature(
        self.view.FILTER)
    out = TreeMap()
    for spec, value in six.iteritems(filters_map):
        if spec[0] == '-':
            spec = spec[1:]
            inex = '_exclude'
        else:
            inex = '_include'
        if '|' in spec:
            rel, spec = spec.split('|')
            rel = rel.split('.')
        else:
            rel = None
        parts = spec.split('.')
        if len(parts) > 1 and parts[-1] in self.VALID_FILTER_OPERATORS:
            operator = parts.pop()
        else:
            operator = None
        if operator == 'range':
            value = value[:2]
        elif operator == 'in':
            pass
        elif operator in self.VALID_FILTER_OPERATORS:
            value = value[0]
            if operator == 'isnull' and isinstance(value, six.string_types):
                value = is_truthy(value)
            elif operator == 'eq':
                operator = None
        node = FilterNode(parts, operator, value)
        path = rel if rel else []
        path += [inex, node.key]
        out.insert(path, node)
    return out