def _Open(self, path_spec=None, mode='rb'):
    if not path_spec:
        raise ValueError('Missing path specification.')
    if path_spec.HasParent():
        raise errors.PathSpecError(
            'Unsupported path specification with parent.')
    location = getattr(path_spec, 'location', None)
    if location is None:
        raise errors.PathSpecError('Path specification missing location.')
    try:
        is_device = pysmdev.check_device(location)
    except IOError as exception:
        exception_string = str(exception)
        if not isinstance(exception_string, py2to3.UNICODE_TYPE):
            exception_string = py2to3.UNICODE_TYPE(exception_string, errors
                ='replace')
        if ' access denied ' in exception_string:
            raise errors.AccessError(
                'Access denied to file: {0:s} with error: {1!s}'.format(
                location, exception_string))
        is_device = False
    if not is_device:
        try:
            stat_info = os.stat(location)
        except OSError as exception:
            raise IOError('Unable to open file with error: {0!s}.'.format(
                exception))
        if stat.S_ISCHR(stat_info.st_mode) or stat.S_ISBLK(stat_info.st_mode):
            is_device = True
    if is_device:
        self._file_object = pysmdev.handle()
        self._file_object.open(location, mode=mode)
        self._size = self._file_object.media_size
    else:
        self._file_object = open(location, mode=mode)
        self._size = stat_info.st_size