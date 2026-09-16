def get_published(name, config_path=_DEFAULT_CONFIG_PATH, endpoint='',
    prefix=None):
    _validate_config(config_path)
    ret = dict()
    sources = list()
    cmd = ['publish', 'show', '-config={}'.format(config_path), name]
    if prefix:
        cmd.append('{}:{}'.format(endpoint, prefix))
    cmd_ret = _cmd_run(cmd)
    ret = _parse_show_output(cmd_ret=cmd_ret)
    if ret:
        log.debug('Found published repository: %s', name)
    else:
        log.debug('Unable to find published repository: %s', name)
    return ret