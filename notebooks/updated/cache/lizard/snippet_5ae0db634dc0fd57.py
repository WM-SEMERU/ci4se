def worktree_add(cwd, worktree_path, ref=None, reset_branch=None, force=
    None, detach=False, opts='', git_opts='', user=None, password=None,
    ignore_retcode=False, output_encoding=None, **kwargs):
    _check_worktree_support()
    kwargs = salt.utils.args.clean_kwargs(**kwargs)
    branch_ = kwargs.pop('branch', None)
    if kwargs:
        salt.utils.args.invalid_kwargs(kwargs)
    cwd = _expand_path(cwd, user)
    if branch_ and detach:
        raise SaltInvocationError(
            "Only one of 'branch' and 'detach' is allowed")
    command = ['git'] + _format_git_opts(git_opts)
    command.extend(['worktree', 'add'])
    if detach:
        if force:
            log.warning(
                "'force' argument to git.worktree_add is ignored when detach=True"
                )
        command.append('--detach')
    else:
        if not branch_:
            branch_ = os.path.basename(worktree_path)
        command.extend(['-B' if reset_branch else '-b', branch_])
        if force:
            command.append('--force')
    command.extend(_format_opts(opts))
    command.append(worktree_path)
    if ref:
        command.append(ref)
    return _git_run(command, cwd=cwd, user=user, password=password,
        ignore_retcode=ignore_retcode, redirect_stderr=True,
        output_encoding=output_encoding)['stdout']