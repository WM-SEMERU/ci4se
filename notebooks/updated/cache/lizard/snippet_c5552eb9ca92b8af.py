def fix_field_params_repr(params):


    class ReprUnicode(text_type):

        def __new__(cls, text):
            return text_type.__new__(cls, text)

        def __repr__(self):
            out = repr(text_type(self))
            return out[1:] if out.startswith("u'") or out.startswith('u"'
                ) else out


    class ReprChoices(list):

        def __new__(cls, choices):
            return list.__new__(cls, choices)

        def __repr__(self):
            out = []
            for x_0, x_1 in self:
                out.append('(%s, %s)' % (repr(ReprUnicode(x_0) if
                    isinstance(x_0, text_type) else x_0), repr(ReprUnicode(
                    x_1) if isinstance(x_1, text_type) else x_1)))
            return '[%s]' % ', '.join(out)
    if PY3:
        return params
    out = OrderedDict()
    for k, v in params.items():
        if k == 'choices' and v:
            v = ReprChoices(v)
        elif isinstance(v, text_type):
            v = ReprUnicode(v)
        out[k] = v
    return out