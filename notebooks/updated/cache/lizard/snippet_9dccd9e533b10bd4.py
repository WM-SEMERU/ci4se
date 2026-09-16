def install_semod(module_path):
    if module_path.find('salt://') == 0:
        module_path = __salt__['cp.cache_file'](module_path)
    cmd = 'semodule -i {0}'.format(module_path)
    return not __salt__['cmd.retcode'](cmd)