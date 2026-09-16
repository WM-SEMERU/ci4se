def chhome(name, home, **kwargs):
    kwargs = salt.utils.args.clean_kwargs(**kwargs)
    persist = kwargs.pop('persist', False)
    if kwargs:
        salt.utils.args.invalid_kwargs(kwargs)
    if persist:
        log.info("Ignoring unsupported 'persist' argument to user.chhome")
    pre_info = info(name)
    if not pre_info:
        raise CommandExecutionError("User '{0}' does not exist".format(name))
    if home == pre_info['home']:
        return True
    _dscl(['/Users/{0}'.format(name), 'NFSHomeDirectory', pre_info['home'],
        home], ctype='change')
    time.sleep(1)
    return info(name).get('home') == home