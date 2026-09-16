def install_from_zip(pkgpath, install_path, register_func,
    delete_after_install=False):
    logger.debug('%s is a file, attempting to load zip', pkgpath)
    pkgtempdir = tempfile.mkdtemp(prefix='honeycomb_')
    try:
        with zipfile.ZipFile(pkgpath) as pkgzip:
            pkgzip.extractall(pkgtempdir)
    except zipfile.BadZipfile as exc:
        logger.debug(str(exc))
        raise click.ClickException(str(exc))
    if delete_after_install:
        logger.debug('deleting %s', pkgpath)
        os.remove(pkgpath)
    logger.debug('installing from unzipped folder %s', pkgtempdir)
    return install_dir(pkgtempdir, install_path, register_func,
        delete_after_install=True)