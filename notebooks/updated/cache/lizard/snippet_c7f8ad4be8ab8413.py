def setup_user_mapping(pid, uid=os.getuid(), gid=os.getgid()):
    proc_child = os.path.join('/proc', str(pid))
    try:
        uid_map = '{0} {1} 1'.format(uid, os.getuid())
        util.write_file(uid_map, proc_child, 'uid_map')
    except IOError as e:
        logging.warning('Creating UID mapping into container failed: %s', e)
    try:
        util.write_file('deny', proc_child, 'setgroups')
    except IOError as e:
        if e.errno != errno.ENOENT:
            logging.warning('Could not write to setgroups file in /proc: %s', e
                )
    try:
        gid_map = '{0} {1} 1'.format(gid, os.getgid())
        util.write_file(gid_map, proc_child, 'gid_map')
    except IOError as e:
        logging.warning('Creating GID mapping into container failed: %s', e)