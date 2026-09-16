def undo(config='root', files=None, num_pre=None, num_post=None):
    pre, post = _get_num_interval(config, num_pre, num_post)
    changes = status(config, pre, post)
    changed = set(changes.keys())
    requested = set(files or changed)
    if not requested.issubset(changed):
        raise CommandExecutionError(
            'Given file list contains files that are not presentin the changed filelist: {0}'
            .format(changed - requested))
    cmdret = __salt__['cmd.run']('snapper -c {0} undochange {1}..{2} {3}'.
        format(config, pre, post, ' '.join(requested)))
    try:
        components = cmdret.split(' ')
        ret = {}
        for comp in components:
            key, val = comp.split(':')
            ret[key] = val
        return ret
    except ValueError as exc:
        raise CommandExecutionError(
            'Error while processing Snapper response: {0}'.format(cmdret))