def _get_program_dir(name, config):
    if config is None:
        raise ValueError('Could not find directory in config for %s' % name)
    elif isinstance(config, six.string_types):
        return config
    elif 'dir' in config:
        return expand_path(config['dir'])
    else:
        raise ValueError('Could not find directory in config for %s' % name)