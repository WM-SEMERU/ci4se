def _multiline_convert(config, start='banner login', end='EOF', depth=1):
    ret = list(config)
    try:
        s = ret.index(start)
        e = s
        while depth:
            e = ret.index(end, e + 1)
            depth = depth - 1
    except ValueError:
        return ret
    ret[s] = {'cmd': ret[s], 'input': '\n'.join(ret[s + 1:e])}
    del ret[s + 1:e + 1]
    return ret