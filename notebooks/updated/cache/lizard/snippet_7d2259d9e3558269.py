def config(config, fork_name='', origin_name=''):
    state = read(config.configfile)
    any_set = False
    if fork_name:
        update(config.configfile, {'FORK_NAME': fork_name})
        success_out('fork-name set to: {}'.format(fork_name))
        any_set = True
    if origin_name:
        update(config.configfile, {'ORIGIN_NAME': origin_name})
        success_out('origin-name set to: {}'.format(origin_name))
        any_set = True
    if not any_set:
        info_out('Fork-name: {}'.format(state['FORK_NAME']))