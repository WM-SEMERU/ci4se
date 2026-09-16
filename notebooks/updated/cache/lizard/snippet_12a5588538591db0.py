def _initialize_repo_cache():
    LOGGER.info('Initializing repository cache')
    repo_cache = {}
    for hit in GitRepo.search().query('match_all').scan():
        repo_cache[hit.repo_name] = hit.to_dict(skip_empty=False)
    return repo_cache