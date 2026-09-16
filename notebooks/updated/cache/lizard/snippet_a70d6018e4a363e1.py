def config(name, config, write=True):
    _build_config_tree(name, config)
    configs = _render_configuration()
    if __opts__.get('test', False):
        comment = "State syslog_ng will write '{0}' into {1}".format(configs,
            __SYSLOG_NG_CONFIG_FILE)
        return _format_state_result(name, result=None, comment=comment)
    succ = write
    if write:
        succ = _write_config(config=configs)
    return _format_state_result(name, result=succ, changes={'new': configs,
        'old': ''})