def install(pkg, dir, pkgs=None, runas=None, env=None):
    _check_valid_version()
    cmd = _construct_bower_command('install')
    if pkg:
        cmd.append(pkg)
    elif pkgs:
        cmd.extend(pkgs)
    result = __salt__['cmd.run_all'](cmd, cwd=dir, runas=runas, env=env,
        python_shell=False)
    if result['retcode'] != 0:
        raise CommandExecutionError(result['stderr'])
    stdout = salt.utils.json.loads(result['stdout'])
    return stdout != {}