def setup_and_get_default_path(self, jar_base_filename):
    import os
    import errno
    install_dir = os.path.expanduser(INSTALL_DIR)
    try:
        os.makedirs(install_dir)
    except OSError as ose:
        if ose.errno != errno.EEXIST:
            raise ose
    jar_filename = os.path.join(install_dir, jar_base_filename)
    return jar_filename