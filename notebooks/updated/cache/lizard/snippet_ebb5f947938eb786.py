def check(cls, dic):
    res = {}
    for name, text in dic.items():
        try:
            p = getattr(cls, name)
        except AttributeError:
            logging.warning('Ignored unknown parameter %s', name)
        else:
            res[name] = p.validator(text)
    return res