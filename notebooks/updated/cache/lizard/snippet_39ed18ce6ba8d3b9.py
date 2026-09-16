def load(path):
    ret = False
    cmd = 'vmctl load {0}'.format(path)
    result = __salt__['cmd.run_all'](cmd, output_loglevel='trace',
        python_shell=False)
    if result['retcode'] == 0:
        ret = True
    else:
        raise CommandExecutionError('Problem encountered running vmctl',
            info={'errors': [result['stderr']], 'changes': ret})
    return ret