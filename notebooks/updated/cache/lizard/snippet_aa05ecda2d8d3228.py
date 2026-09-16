def _check_keys(self, rdict):
    if '_meta_data' in rdict:
        error_message = (
            """Response contains key '_meta_data' which is incompatible with this API!!
 Response json: %r"""
             % rdict)
        raise DeviceProvidesIncompatibleKey(error_message)
    for x in rdict:
        if not re.match(tokenize.Name, x):
            error_message = (
                "Device provided %r which is disallowed because it's not a valid Python 2.7 identifier."
                 % x)
            raise DeviceProvidesIncompatibleKey(error_message)
        elif keyword.iskeyword(x):
            rdict[x + '_'] = rdict[x]
            rdict.pop(x)
        elif x.startswith('__'):
            error_message = (
                'Device provided %r which is disallowed, it mangles into a Python non-public attribute.'
                 % x)
            raise DeviceProvidesIncompatibleKey(error_message)
    return rdict