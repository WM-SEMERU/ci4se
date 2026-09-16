def _get_assistive_access():
    cmd = (
        'sqlite3 "/Library/Application Support/com.apple.TCC/TCC.db" "SELECT * FROM access"'
        )
    call = __salt__['cmd.run_all'](cmd, output_loglevel='debug',
        python_shell=False)
    if call['retcode'] != 0:
        comment = ''
        if 'stderr' in call:
            comment += call['stderr']
        if 'stdout' in call:
            comment += call['stdout']
        raise CommandExecutionError('Error: {0}'.format(comment))
    out = call['stdout']
    return re.findall(
        'kTCCServiceAccessibility\\|(.*)\\|[0-9]{1}\\|([0-9]{1})\\|[0-9]{1}\\|'
        , out, re.MULTILINE)