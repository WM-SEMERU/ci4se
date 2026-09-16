def resolve(container, expression):
    itemgetter = getattr(container, 'get_item', container.get)
    tokens = []
    expression = expression.strip()
    for sel_delim, _id, _range in selection_re.findall(expression):
        tokens.append(delimiters.get(sel_delim, ''))
        item = itemgetter(_id)
        if item is None:
            raise XigtStructureError(
                'Referred Item (id: {}) from reference "{}" does not exist in the given container.'
                .format(_id, expression))
        value = item.value() or ''
        if _range:
            for spn_delim, start, end in span_re.findall(_range):
                start = int(start) if start else None
                end = int(end) if end else None
                tokens.extend([delimiters.get(spn_delim, ''), value[start:end]]
                    )
        else:
            tokens.append(value)
    return ''.join(tokens)