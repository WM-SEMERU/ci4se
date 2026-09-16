def make_dir(dir_name, linux_mode=493, error_if_not_writable=False):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name, linux_mode)
    elif error_if_not_writable:
        if not os.access(dir_name, os.R_OK | os.W_OK | os.X_OK):
            raise IOError('Directory {0} is not writable.'.format(dir_name))