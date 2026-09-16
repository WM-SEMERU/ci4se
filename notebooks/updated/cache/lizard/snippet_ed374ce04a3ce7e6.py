def find_file(path, tgt_env='base', **kwargs):
    fnd = {'path': '', 'rel': ''}
    if os.path.isabs(path) or tgt_env not in envs():
        return fnd
    for repo in init():
        env_root = _env_root(repo, tgt_env)
        if env_root is None:
            continue
        if repo['mountpoint'] and not path.startswith(repo['mountpoint'] +
            os.path.sep):
            continue
        repo_path = path[len(repo['mountpoint']):].lstrip(os.path.sep)
        if repo['root']:
            repo_path = os.path.join(repo['root'], repo_path)
        full = os.path.join(env_root, repo_path)
        if os.path.isfile(full):
            fnd['rel'] = path
            fnd['path'] = full
            try:
                fnd['stat'] = list(os.stat(full))
            except Exception:
                pass
            return fnd
    return fnd