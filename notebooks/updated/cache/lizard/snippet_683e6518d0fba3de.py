def get_exdesc():
    fname = inspect.getframeinfo(sys._getframe(1))[2]
    count = 0
    fobj = None
    while not (fobj and hasattr(fobj, 'exdesc')):
        count = count + 1
        try:
            sitem = sys._getframe(count)
        except ValueError:
            raise RuntimeError(
                'Function object could not be found for function `{0}`'.
                format(fname))
        fobj = sitem.f_locals[fname
            ] if fname in sitem.f_locals else sitem.f_globals[fname
            ] if fname in sitem.f_globals else None
    exdesc = getattr(fobj, 'exdesc')
    return exdesc if len(exdesc) > 1 else exdesc[next(iter(exdesc))]