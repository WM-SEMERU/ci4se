def cli(dirty, stash):
    _setup_logging()
    LOGGER.info('EPAB %s', __version__)
    LOGGER.info('Running in %s', os.getcwd())
    CTX.repo = epab.utils.Repo()
    CTX.repo.ensure()
    CTX.stash = stash
    for filename in _GIT_IGNORE:
        epab.utils.add_to_gitignore(filename)
    if not dirty and CTX.repo.is_dirty():
        LOGGER.error('Repository is dirty')
        sys.exit(-1)