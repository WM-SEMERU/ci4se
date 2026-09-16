def pprint(val, imports, prefix='\n    ', settings=[], unknown_value='<?>',
    qualify=False, separator=''):
    if isinstance(val, type):
        rep = type_script_repr(val, imports, prefix, settings)
    elif type(val) in script_repr_reg:
        rep = script_repr_reg[type(val)](val, imports, prefix, settings)
    elif hasattr(val, 'script_repr'):
        rep = val.script_repr(imports, prefix + '    ')
    elif hasattr(val, 'pprint'):
        rep = val.pprint(imports=imports, prefix=prefix + '    ', qualify=
            qualify, unknown_value=unknown_value, separator=separator)
    else:
        rep = repr(val)
    return rep