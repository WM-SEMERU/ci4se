def printable_name(column, path=None):
    pieces = [column.name]
    path = path or path_of(column)
    for segment in path:
        if isinstance(segment, str):
            pieces.append(segment)
        else:
            pieces[-1] += '[{}]'.format(segment)
    return '.'.join(pieces)