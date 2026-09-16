def file_dict(*packages, **kwargs):
    errors = []
    ret = {}
    cmd_files = ['opkg', 'files']
    if not packages:
        packages = list(list_pkgs().keys())
    for package in packages:
        files = []
        cmd = cmd_files[:]
        cmd.append(package)
        out = __salt__['cmd.run_all'](cmd, output_loglevel='trace',
            python_shell=False)
        for line in out['stdout'].splitlines():
            if line.startswith('/'):
                files.append(line)
            elif line.startswith(' * '):
                errors.append(line[3:])
                break
            else:
                continue
        if files:
            ret[package] = files
    return {'errors': errors, 'packages': ret}