def _authGetDBusCookie(self, cookie_context, cookie_id):
    if self.cookie_dir is None:
        cookie_dir = os.path.expanduser('~/.dbus-keyrings')
    else:
        cookie_dir = self.cookie_dir
    dstat = os.stat(cookie_dir)
    if dstat.st_mode & 54:
        raise Exception(
            'User keyrings directory is writeable by other users. Aborting authentication'
            )
    import pwd
    if dstat.st_uid != pwd.getpwuid(os.geteuid()).pw_uid:
        raise Exception(
            'Keyrings directory is not owned by the current user. Aborting authentication!'
            )
    f = open(os.path.join(cookie_dir, cookie_context), 'r')
    try:
        for line in f:
            try:
                k_id, k_time, k_cookie_hex = line.split()
                if k_id == cookie_id:
                    return k_cookie_hex
            except:
                pass
    finally:
        f.close()