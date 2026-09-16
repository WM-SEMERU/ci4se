def _change_source_state(name, state):
    choc_path = _find_chocolatey(__context__, __salt__)
    cmd = [choc_path, 'source', state, '--name', name]
    result = __salt__['cmd.run_all'](cmd, python_shell=False)
    if result['retcode'] != 0:
        raise CommandExecutionError('Running chocolatey failed: {0}'.format
            (result['stdout']))
    return result['stdout']