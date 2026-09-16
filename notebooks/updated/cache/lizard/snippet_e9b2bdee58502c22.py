def nexec(statement, globals=None, locals=None, **kwargs):
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins
    from ast import parse
    from napi.transformers import NapiTransformer
    from ast import fix_missing_locations as fml
    try:
        node = parse(statement, '<string>', 'exec')
    except ImportError:
        exec(statement)
    else:
        if globals is None:
            globals = builtins.globals()
        if locals is None:
            locals = {}
        trans = NapiTransformer(globals=globals, locals=locals, **kwargs)
        trans.visit(node)
        code = compile(fml(node), '<string>', 'exec')
        return builtins.eval(code, globals, locals)