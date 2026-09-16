def execute_return_success(cmd):
    ret = _run_all(cmd)
    if ret['retcode'] != 0 or 'not supported' in ret['stdout'].lower():
        msg = 'Command Failed: {0}\n'.format(cmd)
        msg += 'Return Code: {0}\n'.format(ret['retcode'])
        msg += 'Output: {0}\n'.format(ret['stdout'])
        msg += 'Error: {0}\n'.format(ret['stderr'])
        raise CommandExecutionError(msg)
    return True