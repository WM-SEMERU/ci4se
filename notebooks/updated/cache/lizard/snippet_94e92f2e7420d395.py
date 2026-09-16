def read_plain_text(fname, encoding='utf-8'):
    with io.open(fname, encoding=encoding) as f:
        result = list(f)
    if result:
        if result[-1][-1:] == '\n':
            result.append('\n')
        else:
            result[-1] += '\n'
        return [line[:-1] for line in result]
    return []