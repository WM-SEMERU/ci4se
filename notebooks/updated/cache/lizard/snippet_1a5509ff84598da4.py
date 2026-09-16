def _resolve_multi(self, interpreter, requirements, platforms, find_links):
    python_setup = self._python_setup_subsystem
    python_repos = self._python_repos_subsystem
    platforms = platforms or python_setup.platforms
    find_links = find_links or []
    distributions = {}
    fetchers = python_repos.get_fetchers()
    fetchers.extend(Fetcher([path]) for path in find_links)
    for platform in platforms:
        requirements_cache_dir = os.path.join(python_setup.
            resolver_cache_dir, str(interpreter.identity))
        resolved_dists = resolve(requirements=[str(req.requirement) for req in
            requirements], interpreter=interpreter, fetchers=fetchers,
            platform=platform, context=python_repos.get_network_context(),
            cache=requirements_cache_dir, cache_ttl=python_setup.
            resolver_cache_ttl, allow_prereleases=python_setup.
            resolver_allow_prereleases, use_manylinux=python_setup.
            use_manylinux)
        distributions[platform] = [resolved_dist.distribution for
            resolved_dist in resolved_dists]
    return distributions