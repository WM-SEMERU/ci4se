def merge(cwd, rev=None, opts='', git_opts='', user=None, password=None,
    identity=None, ignore_retcode=False, output_encoding=None, **kwargs):
    kwargs = salt.utils.args.clean_kwargs(**kwargs)
    if kwargs:
        salt.utils.args.invalid_kwargs(kwargs)
    cwd = _expand_path(cwd, user)
    command = ['git'] + _format_git_opts(git_opts)
    command.append('merge')
    command.extend(_format_opts(opts))
    if rev:
        command.append(rev)
    return _git_run(command, cwd=cwd, user=user, password=password,
        identity=identity, ignore_retcode=ignore_retcode, output_encoding=
        output_encoding)['stdout']