def online(note, github_repository, github_username):
    callbacks.git_installed()
    try:
        repo = git.Repo()
    except git.InvalidGitRepositoryError:
        LOGGER.critical(
            "'memote online' requires a git repository in order to follow the current branch's commit history."
            )
        sys.exit(1)
    if note == 'memote-ci access':
        note = '{} to {}'.format(note, github_repository)
    gh_repo_name, auth_token, repo_access_token = _setup_gh_repo(
        github_repository, github_username, note)
    secret = _setup_travis_ci(gh_repo_name, auth_token, repo_access_token)
    LOGGER.info("Storing GitHub token in '.travis.yml'.")
    config = te.load_travis_configuration('.travis.yml')
    global_env = config.setdefault('env', {}).get('global')
    if global_env is None:
        config['env']['global'] = global_env = {}
    try:
        global_env['secure'] = secret
    except TypeError:
        global_env.append({'secure': secret})
    te.dump_travis_configuration(config, '.travis.yml')
    LOGGER.info("Add, commit and push changes to '.travis.yml' to GitHub.")
    repo.index.add(['.travis.yml'])
    check_call(['git', 'commit', '-m',
        'chore: add encrypted GitHub access token'])
    check_call(['git', 'push', '--set-upstream', 'origin', repo.
        active_branch.name])