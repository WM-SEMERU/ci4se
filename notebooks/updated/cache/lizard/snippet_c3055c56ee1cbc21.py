def from_string(self, value):
    if value.startswith('[') and value.endswith(']'):
        text = value[1:-1].strip()
    else:
        text = value.strip()
    result = []
    if text.startswith('('):
        tokens = text.split(',')
        if len(tokens) % 2 != 0:
            raise ValueError('not a valid list of pairs')
        pos = 0
        while pos < len(tokens):
            val1 = float(tokens[pos].strip()[1:].strip())
            val2 = float(tokens[pos + 1].strip()[:-1])
            result.append((val1, val2))
            pos += 2
    else:
        for val in text.split(','):
            result.append(float(val))
    if len(result) < 2:
        raise ValueError('invalid number of elements in list: ' + str(len(
            result)))
    return result