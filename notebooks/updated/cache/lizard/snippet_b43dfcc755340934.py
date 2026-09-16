def get_module_functions(modules):
    module_fns = set()
    for module in modules:
        for key in dir(module):
            attr = getattr(module, key)
            if isinstance(attr, (types.BuiltinFunctionType, types.
                FunctionType, numpy.ufunc)):
                module_fns.add(attr)
    return module_fns