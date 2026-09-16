def is_installed(name):
    out = __salt__['cmd.run_all'](FLATPAK_BINARY_NAME + ' info ' + name)
    if out['retcode'] and out['stderr']:
        return False
    else:
        return True