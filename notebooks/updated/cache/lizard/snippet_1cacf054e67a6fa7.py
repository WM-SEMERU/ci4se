def _validator(key, val, env):
    if not env[key] in (True, False):
        raise SCons.Errors.UserError(
            'Invalid value for boolean option %s: %s' % (key, env[key]))