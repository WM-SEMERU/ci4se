def _build_indices(self):
    result = {key: OrderedDict() for key in LINES_WITH_ID}
    for line in self.lines:
        if line.key in LINES_WITH_ID:
            result.setdefault(line.key, OrderedDict())
            if line.mapping['ID'] in result[line.key]:
                warnings.warn(
                    'Seen {} header more than once: {}, using firstoccurence'
                    .format(line.key, line.mapping['ID']),
                    DuplicateHeaderLineWarning)
            else:
                result[line.key][line.mapping['ID']] = line
        else:
            result.setdefault(line.key, [])
            result[line.key].append(line)
    return result