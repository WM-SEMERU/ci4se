def download_pip_based_installations(env, pip_invocation, requirements,
    download_cache_folder):
    if config.installation_cache_folder() is None:
        raise EnvironmentSetupError(
            'Local installation cache folder not defined but required for downloading pip based installations.'
            )
    _create_installation_cache_folder_if_needed()
    try:
        pip_options = ['install', '-d', config.installation_cache_folder(),
            '--exists-action=i']
        pip_options.extend(pip_download_cache_options(download_cache_folder))
        if (2, 5) <= env.sys_version_info < (2, 6):
            pip_options.append('--insecure')
        env.execute(pip_invocation + pip_options + requirements)
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception:
        raise EnvironmentSetupError('pip based download failed.')