def from_py_func(cls, func):
    from bokeh.util.deprecation import deprecated
    deprecated(
        "'from_py_func' is deprecated and will be removed in an eventual 2.0 release. Use CustomJS directly instead."
        )
    if not isinstance(func, FunctionType):
        raise ValueError('CustomJS.from_py_func needs function object.')
    pscript = import_required('pscript', 
        'To use Python functions for CustomJS, you need PScript ' +
        '("conda install -c conda-forge pscript" or "pip install pscript")')
    default_values = func.__defaults__
    default_names = func.__code__.co_varnames[:len(default_values)]
    args = dict(zip(default_names, default_values))
    args.pop('window', None)
    code = pscript.py2js(func, 'cb') + 'cb(%s);\n' % ', '.join(default_names)
    return cls(code=code, args=args)