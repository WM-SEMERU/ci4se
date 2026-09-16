def load_configs(files, cwd=os.getcwd()):
    repos = []
    for f in files:
        _, ext = os.path.splitext(f)
        conf = kaptan.Kaptan(handler=ext.lstrip('.')).import_config(f)
        newrepos = extract_repos(conf.export('dict'), cwd)
        if not repos:
            repos.extend(newrepos)
            continue
        dupes = detect_duplicate_repos(repos, newrepos)
        if dupes:
            msg = 'repos with same path + different VCS detected!', dupes
            raise exc.VCSPullException(msg)
        repos.extend(newrepos)
    return repos