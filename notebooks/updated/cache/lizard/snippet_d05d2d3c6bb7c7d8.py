def install(ctx, plugin):
    ensure_inside_venv(ctx)
    plugin_name = get_plugin_name(plugin)
    try:
        info = get_plugin_info(plugin_name)
    except NameError:
        echo_error('Plugin {} could not be found.'.format(plugin))
        sys.exit(1)
    except ValueError as e:
        echo_error('Unable to retrieve plugin info. Error was:\n\n {}'.
            format(e))
        sys.exit(1)
    try:
        installed_version = pkg_resources.get_distribution(plugin_name).version
    except pkg_resources.DistributionNotFound:
        installed_version = None
    if installed_version is not None and info['version'] == installed_version:
        click.echo('You already have the latest version of {} ({}).'.format
            (plugin, info['version']))
        return
    pinned_plugin = '{0}=={1}'.format(plugin_name, info['version'])
    try:
        run_command([sys.executable, '-m', 'pip', 'install', pinned_plugin])
    except subprocess.CalledProcessError as e:
        echo_error('Error when trying to install plugin {}. Error was:\n\n {}'
            .format(plugin, e))
        sys.exit(1)
    echo_success('Plugin {} {} installed successfully.'.format(plugin, info
        ['version']))