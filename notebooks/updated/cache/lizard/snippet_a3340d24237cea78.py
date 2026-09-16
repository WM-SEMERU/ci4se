def dumps(obj, pretty=False, escaped=True):
    if not isinstance(obj, dict):
        raise TypeError('Expected data to be an instance of``dict``')
    if not isinstance(pretty, bool):
        raise TypeError('Expected pretty to be of type bool')
    if not isinstance(escaped, bool):
        raise TypeError('Expected escaped to be of type bool')
    return ''.join(_dump_gen(obj, pretty, escaped))