def run_command(provider, context, command, capture=False, interactive=
    False, ignore_status=False, quiet=False, stdin=None, env=None, **kwargs):
    if quiet and capture:
        raise ImproperlyConfigured(__name__ + '.run_command',
            'Cannot enable `quiet` and `capture` options simultaneously')
    if quiet:
        out_err_type = _devnull()
    elif capture:
        out_err_type = PIPE
    else:
        out_err_type = None
    if interactive:
        in_type = None
    elif stdin:
        in_type = PIPE
    else:
        in_type = _devnull()
    if env:
        full_env = os.environ.copy()
        full_env.update(env)
        env = full_env
    logger.info('Running command: %s', command)
    proc = Popen(command, stdin=in_type, stdout=out_err_type, stderr=
        out_err_type, env=env, **kwargs)
    try:
        out, err = proc.communicate(stdin)
        status = proc.wait()
        if status == 0 or ignore_status:
            return {'returncode': proc.returncode, 'stdout': out, 'stderr': err
                }
        if logger.isEnabledFor(logging.INFO):
            logger.warn('Command failed with returncode %d', status)
        else:
            logger.warn('Command failed with returncode %d: %s', status,
                command)
        return None
    finally:
        if proc.returncode is None:
            proc.kill()