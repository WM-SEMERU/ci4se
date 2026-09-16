def remove_repo(name, profile='github'):
    repo_info = get_repo_info(name, profile=profile)
    if not repo_info:
        log.error('Repo %s to be removed does not exist.', name)
        return False
    try:
        client = _get_client(profile)
        organization = client.get_organization(_get_config_value(profile,
            'org_name'))
        repo = organization.get_repo(name)
        repo.delete()
        _get_repos(profile=profile, ignore_cache=True)
        return True
    except github.GithubException:
        log.exception('Error deleting a repo')
        return False