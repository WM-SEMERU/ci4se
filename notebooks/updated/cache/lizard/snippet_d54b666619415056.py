def estimate(path):
    if not os.path.exists(path):
        raise CommandExecutionError('Path "{0}" was not found.'.format(path))
    out = __salt__['cmd.run_all']('xfs_estimate -v {0}'.format(path))
    _verify_run(out)
    return _xfs_estimate_output(out['stdout'])