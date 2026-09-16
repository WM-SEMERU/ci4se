def set_repo(name, config_path=_DEFAULT_CONFIG_PATH, comment=None,
    component=None, distribution=None, uploaders_file=None, saltenv='base'):
    _validate_config(config_path)
    failed_settings = dict()
    settings = {'comment': comment, 'component': component, 'distribution':
        distribution}
    for setting in list(settings):
        if settings[setting] is None:
            settings.pop(setting, None)
    current_settings = __salt__['aptly.get_repo'](name=name, config_path=
        config_path)
    if not current_settings:
        log.error('Unable to get repo: %s', name)
        return False
    for current_setting in list(current_settings):
        if current_setting not in settings:
            current_settings.pop(current_setting, None)
    if settings == current_settings:
        log.debug('Settings already have the desired values for repository: %s'
            , name)
        return True
    cmd = ['repo', 'edit', '-config={}'.format(config_path)]
    repo_params = _format_repo_args(comment=comment, component=component,
        distribution=distribution, uploaders_file=uploaders_file, saltenv=
        saltenv)
    cmd.extend(repo_params)
    cmd.append(name)
    _cmd_run(cmd)
    new_settings = __salt__['aptly.get_repo'](name=name, config_path=
        config_path)
    for setting in settings:
        if settings[setting] != new_settings[setting]:
            failed_settings.update({setting: settings[setting]})
    if failed_settings:
        log.error('Unable to change settings for the repository: %s', name)
        return False
    log.debug(
        'Settings successfully changed to the desired values for repository: %s'
        , name)
    return True