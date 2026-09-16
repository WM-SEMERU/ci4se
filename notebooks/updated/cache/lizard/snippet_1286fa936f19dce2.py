def install_from_repo(pkgname, plugin_type, install_path, register_func):
    rsession = requests.Session()
    rsession.mount('https://', HTTPAdapter(max_retries=3))
    logger.debug('trying to install %s from online repo', pkgname)
    pkgurl = '{}/{}s/{}.zip'.format(defs.GITHUB_RAW, plugin_type, pkgname)
    try:
        logger.debug('Requesting HTTP HEAD: %s', pkgurl)
        r = rsession.head(pkgurl)
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))
        pkgsize = _sizeof_fmt(total_size)
        with click.progressbar(length=total_size, label=
            'Downloading {} {} ({})..'.format(plugin_type, pkgname, pkgsize)
            ) as bar:
            r = rsession.get(pkgurl, stream=True)
            with tempfile.NamedTemporaryFile(delete=False) as f:
                downloaded_bytes = 0
                for chunk in r.iter_content(chunk_size=1):
                    if chunk:
                        f.write(chunk)
                        downloaded_bytes += len(chunk)
                        bar.update(downloaded_bytes)
        return install_from_zip(f.name, install_path, register_func,
            delete_after_install=True)
    except requests.exceptions.HTTPError as exc:
        logger.debug(str(exc))
        raise exceptions.PluginNotFoundInOnlineRepo(pkgname)
    except requests.exceptions.ConnectionError as exc:
        logger.debug(str(exc))
        raise exceptions.PluginRepoConnectionError()