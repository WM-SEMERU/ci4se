def ssh_wrapper(opts, functions=None, context=None):
    return LazyLoader(_module_dirs(opts, 'wrapper', base_path=os.path.join(
        SALT_BASE_PATH, os.path.join('client', 'ssh'))), opts, tag=
        'wrapper', pack={'__salt__': functions, '__grains__': opts.get(
        'grains', {}), '__pillar__': opts.get('pillar', {}), '__context__':
        context})