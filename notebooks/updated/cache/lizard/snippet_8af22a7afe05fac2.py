def _dict_from_lines(lines, key_nums, sep=None):
    if is_string(lines):
        lines = [lines]
    if not isinstance(key_nums, collections.abc.Iterable):
        key_nums = list(key_nums)
    if len(lines) != len(key_nums):
        err_msg = 'lines = %s\n key_num =  %s' % (str(lines), str(key_nums))
        raise ValueError(err_msg)
    kwargs = Namespace()
    for i, nk in enumerate(key_nums):
        if nk == 0:
            continue
        line = lines[i]
        tokens = [t.strip() for t in line.split()]
        values, keys = tokens[:nk], ''.join(tokens[nk:])
        keys.replace('[', '').replace(']', '')
        keys = keys.split(',')
        if sep is not None:
            check = keys[0][0]
            if check != sep:
                raise ValueError('Expecting separator %s, got %s' % (sep,
                    check))
            keys[0] = keys[0][1:]
        if len(values) != len(keys):
            msg = (
                'line: %s\n len(keys) != len(value)\nkeys: %s\n values: %s' %
                (line, keys, values))
            raise ValueError(msg)
        kwargs.update(zip(keys, values))
    return kwargs