def _safe_hasattr(o, attr):
    try:
        has = hasattr(o, attr)
    except:
        has = False
        msg.err('_safe_hasattr: {}.{}'.format(o, attr), 2)
        pass
    return has