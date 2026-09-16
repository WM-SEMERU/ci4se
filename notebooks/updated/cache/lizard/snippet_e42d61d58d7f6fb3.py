def color_is_forced(**envars):
    result = env.CLICOLOR_FORCE and env.CLICOLOR_FORCE != '0'
    log.debug('%s (CLICOLOR_FORCE=%s)', result, env.CLICOLOR_FORCE or '')
    for name, value in envars.items():
        envar = getattr(env, name)
        if envar.value == value:
            result = True
        log.debug('%s == %r: %r', name, value, result)
    return result