def refresh_db(**kwargs):
    r
    salt.utils.pkg.clear_rtag(__opts__)
    saltenv = kwargs.pop('saltenv', 'base')
    verbose = salt.utils.data.is_true(kwargs.pop('verbose', False))
    failhard = salt.utils.data.is_true(kwargs.pop('failhard', True))
    __context__.pop('winrepo.data', None)
    repo_details = _get_repo_details(saltenv)
    log.debug(
        "Refreshing pkg metadata db for saltenv '%s' (age of existing metadata is %s)"
        , saltenv, datetime.timedelta(seconds=repo_details.winrepo_age))
    log.info("Removing all *.sls files under '%s'", repo_details.local_dest)
    failed = []
    for root, _, files in salt.utils.path.os_walk(repo_details.local_dest,
        followlinks=False):
        for name in files:
            if name.endswith('.sls'):
                full_filename = os.path.join(root, name)
                try:
                    os.remove(full_filename)
                except OSError as exc:
                    if exc.errno != errno.ENOENT:
                        log.error('Failed to remove %s: %s', full_filename, exc
                            )
                        failed.append(full_filename)
    if failed:
        raise CommandExecutionError(
            'Failed to clear one or more winrepo cache files', info={
            'failed': failed})
    log.info('Fetching *.sls files from %s', repo_details.winrepo_source_dir)
    __salt__['cp.cache_dir'](path=repo_details.winrepo_source_dir, saltenv=
        saltenv, include_pat='*.sls', exclude_pat='E@\\/\\..*?\\/')
    return genrepo(saltenv=saltenv, verbose=verbose, failhard=failhard)