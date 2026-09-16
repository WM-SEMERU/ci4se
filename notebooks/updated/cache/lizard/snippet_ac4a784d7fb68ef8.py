def mkdir_p(self, path):
    try:
        if not os.path.isdir(path):
            os.makedirs(path)
            self.log.info('Created Directory [ %s ]', path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise OSError(
                'The provided path can not be created into a directory.')