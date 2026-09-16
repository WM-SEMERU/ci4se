def chmod(path, mode, recursive=False):
    log = logging.getLogger(mod_logger + '.chmod')
    if not isinstance(path, basestring):
        msg = 'path argument is not a string'
        log.error(msg)
        raise CommandError(msg)
    if not isinstance(mode, basestring):
        msg = 'mode argument is not a string'
        log.error(msg)
        raise CommandError(msg)
    if not os.path.exists(path):
        msg = 'Item not found: {p}'.format(p=path)
        log.error(msg)
        raise CommandError(msg)
    command = ['chmod']
    if recursive:
        command.append('-R')
    command.append(mode)
    command.append(path)
    try:
        result = run_command(command)
    except CommandError:
        raise
    log.info('chmod command exited with code: {c}'.format(c=result['code']))
    return result['code']