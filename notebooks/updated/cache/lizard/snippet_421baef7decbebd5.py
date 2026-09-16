def latexify(obj, **kwargs):
    if hasattr(obj, '__pk_latex__'):
        return obj.__pk_latex__(**kwargs)
    if isinstance(obj, text_type):
        from .unicode_to_latex import unicode_to_latex
        return unicode_to_latex(obj)
    if isinstance(obj, bool):
        raise ValueError('no well-defined LaTeXification of bool %r' % obj)
    if isinstance(obj, float):
        nplaces = kwargs.get('nplaces')
        if nplaces is None:
            return '$%f$' % obj
        return '$%.*f$' % (nplaces, obj)
    if isinstance(obj, int):
        return '$%d$' % obj
    if isinstance(obj, binary_type):
        if all(c in _printable_ascii for c in obj):
            return obj.decode('ascii')
        raise ValueError('no safe LaTeXification of binary string %r' % obj)
    raise ValueError("can't LaTeXify %r" % obj)