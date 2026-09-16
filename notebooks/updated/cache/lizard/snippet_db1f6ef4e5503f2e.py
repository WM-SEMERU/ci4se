def configured(name, data, **kwargs):
    models = kwargs.get('models', None)
    if isinstance(models, tuple) and isinstance(models[0], list):
        models = models[0]
    ret = salt.utils.napalm.default_ret(name)
    test = kwargs.get('test', False) or __opts__.get('test', False)
    debug = kwargs.get('debug', False) or __opts__.get('debug', False)
    commit = kwargs.get('commit', True) or __opts__.get('commit', True)
    replace = kwargs.get('replace', False) or __opts__.get('replace', False)
    profiles = kwargs.get('profiles', [])
    if '_kwargs' in data:
        data.pop('_kwargs')
    loaded_changes = __salt__['napalm_yang.load_config'](data, *models,
        profiles=profiles, test=test, debug=debug, commit=commit, replace=
        replace)
    return salt.utils.napalm.loaded_ret(ret, loaded_changes, test, debug)