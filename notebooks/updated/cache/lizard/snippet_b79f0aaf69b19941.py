def list_windowsfeatures():
    choc_path = _find_chocolatey(__context__, __salt__)
    cmd = [choc_path, 'list', '--source', 'windowsfeatures']
    result = __salt__['cmd.run_all'](cmd, python_shell=False)
    if result['retcode'] != 0:
        raise CommandExecutionError('Running chocolatey failed: {0}'.format
            (result['stdout']))
    return result['stdout']