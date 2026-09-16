def _write_secedit_data(inf_data):
    f_sdb = os.path.join(__opts__['cachedir'], 'secedit-{0}.sdb'.format(UUID))
    f_inf = os.path.join(__opts__['cachedir'], 'secedit-{0}.inf'.format(UUID))
    try:
        __salt__['file.write'](f_inf, inf_data)
        cmd = ['secedit', '/configure', '/db', f_sdb, '/cfg', f_inf]
        retcode = __salt__['cmd.retcode'](cmd)
        if retcode == 0:
            __context__.pop('lgpo.secedit_data')
            return True
        return False
    finally:
        if __salt__['file.file_exists'](f_sdb):
            __salt__['file.remove'](f_sdb)
        if __salt__['file.file_exists'](f_inf):
            __salt__['file.remove'](f_inf)