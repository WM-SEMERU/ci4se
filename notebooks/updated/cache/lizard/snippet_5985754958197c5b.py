def _to_colon_ns(bracket_ns, default_ns=None, nsmap=None, snake=True):
    parts = [x.strip('{') for x in bracket_ns.split('}')]
    if len(parts) != 2:
        return bracket_ns
    ns, var = parts
    if default_ns and nsmap:
        try:
            ns = [k for k, v in nsmap.items() if v == ns][0]
            if ns == default_ns:
                if snake:
                    return utils.camel_to_snake(var)
                return var
        except IndexError:
            pass
    if snake:
        return ':'.join([ns, utils.camel_to_snake(var)])
    return ':'.join([ns, var])