def set(*args, **kw):
    if len(args) == 0:
        if len(kw) != 0:
            for keyword, value in kw.items():
                keyword = untranslateName(keyword)
                svalue = str(value)
                _varDict[keyword] = svalue
        else:
            listVars(prefix='    ', equals='=')
    elif len(args) != 1 or len(kw) != 0 or not isinstance(args[0], string_types
        ) or args[0][:1] != '@':
        raise SyntaxError('set requires name=value pairs')