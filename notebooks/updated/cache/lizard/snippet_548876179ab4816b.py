def get(dic, path, seps=PATH_SEPS, idx_reg=_JSNP_GET_ARRAY_IDX_REG):
    items = [_jsnp_unescape(p) for p in _split_path(path, seps)]
    if not items:
        return dic, ''
    try:
        if len(items) == 1:
            return dic[items[0]], ''
        prnt = functools.reduce(operator.getitem, items[:-1], dic)
        arr = anyconfig.utils.is_list_like(prnt) and idx_reg.match(items[-1])
        return (prnt[int(items[-1])], '') if arr else (prnt[items[-1]], '')
    except (TypeError, KeyError, IndexError) as exc:
        return None, str(exc)