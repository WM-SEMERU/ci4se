def isdir(path, message):
    if not os.path.isdir(path):
        raise FileNotFoundError(errno.ENOENT, '{}: {}'.format(message, os.
            strerror(errno.ENOENT)), path)