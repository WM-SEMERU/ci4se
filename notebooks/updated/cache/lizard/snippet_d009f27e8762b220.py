def org_checkout(organization, github_url, github_token, clone_dir, verbose,
    filter, exclude):
    logging.basicConfig(format=
        '%(asctime)s: %(name)s:%(levelname)s %(message)s', level=verbose and
        logging.DEBUG or logging.INFO)
    callbacks = pygit2.RemoteCallbacks(pygit2.UserPass(github_token,
        'x-oauth-basic'))
    repos = []
    for r in github_repos(organization, github_url, github_token):
        if filter:
            found = False
            for f in filter:
                if fnmatch(r['name'], f):
                    found = True
                    break
            if not found:
                continue
        if exclude:
            found = False
            for e in exclude:
                if fnmatch(r['name'], e):
                    found = True
                    break
            if found:
                continue
        repo_path = os.path.join(clone_dir, r['name'])
        repos.append(repo_path)
        if not os.path.exists(repo_path):
            log.debug('Cloning repo: %s/%s' % (organization, r['name']))
            repo = pygit2.clone_repository(r['url'], repo_path, callbacks=
                callbacks)
        else:
            repo = pygit2.Repository(repo_path)
            if repo.status():
                log.warning('repo %s not clean skipping update')
                continue
            log.debug('Syncing repo: %s/%s' % (organization, r['name']))
            pull(repo, callbacks)
    return repos