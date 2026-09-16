def git_commit(targets, message, force=False, sign=False):
    root = get_root()
    target_paths = []
    for t in targets:
        target_paths.append(os.path.join(root, t))
    with chdir(root):
        result = run_command('git add{} {}'.format(' -f' if force else '',
            ' '.join(target_paths)))
        if result.code != 0:
            return result
        return run_command('git commit{} -m "{}"'.format(' -S' if sign else
            '', message))