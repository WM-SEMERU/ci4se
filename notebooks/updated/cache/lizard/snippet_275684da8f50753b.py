def clone_from(repo_url, repo_dir):
    repo_url = _fix_repo_url(repo_url)
    LOG.info('Cloning %s into %s.' % (repo_url, repo_dir))
    cmd = GIT_CLONE_CMD.format(repo_url, repo_dir)
    resp = envoy.run(cmd)
    if resp.status_code != 0:
        LOG.error('Cloned failed: %s' % resp.std_err)
        raise GitException(resp.std_err)
    LOG.info('Clone successful.')