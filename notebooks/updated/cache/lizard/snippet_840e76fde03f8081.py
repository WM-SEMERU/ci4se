def install_plugin(pkgpath, plugin_type, install_path, register_func):
    service_name = os.path.basename(pkgpath)
    if os.path.exists(os.path.join(install_path, service_name)):
        raise exceptions.PluginAlreadyInstalled(pkgpath)
    if os.path.exists(pkgpath):
        logger.debug('%s exists in filesystem', pkgpath)
        if os.path.isdir(pkgpath):
            pip_status = install_dir(pkgpath, install_path, register_func)
        else:
            pip_status = install_from_zip(pkgpath, install_path, register_func)
    else:
        logger.debug('cannot find %s locally, checking github repo', pkgpath)
        click.secho('Collecting {}..'.format(pkgpath))
        pip_status = install_from_repo(pkgpath, plugin_type, install_path,
            register_func)
    if pip_status == 0:
        click.secho('[+] Great success!')
    else:
        click.secho(
            '[-] Service installed but something was odd with dependency install, please review debug logs'
            )