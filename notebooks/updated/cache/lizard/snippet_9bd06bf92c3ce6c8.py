def script_repr(val, imports, prefix, settings):
    return pprint(val, imports, prefix, settings, unknown_value=None,
        qualify=True, separator='\n')