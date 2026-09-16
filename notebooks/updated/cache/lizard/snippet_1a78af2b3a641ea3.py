def program(self, file_or_path, file_format=None, **kwargs):
    isPath = isinstance(file_or_path, six.string_types)
    if isPath and not os.path.isfile(file_or_path):
        raise FileNotFoundError_(errno.ENOENT, "No such file: '{}'".format(
            file_or_path))
    if not file_format:
        if isPath:
            file_format = os.path.splitext(file_or_path)[1][1:]
            if file_format == '':
                raise ValueError(
                    "file path '{}' does not have an extension and no format is set"
                    .format(file_or_path))
        else:
            raise ValueError('file object provided but no format is set')
    if file_format not in self._format_handlers:
        raise ValueError("unknown file format '%s'" % file_format)
    self._loader = FlashLoader(self._session, progress=self._progress,
        chip_erase=self._chip_erase, smart_flash=self._smart_flash,
        trust_crc=self._trust_crc, keep_unwritten=self._keep_unwritten)
    file_obj = None
    try:
        if isPath:
            mode = 'rb'
            if file_format == 'hex':
                mode = 'r'
            file_obj = open(file_or_path, mode)
        else:
            file_obj = file_or_path
        self._format_handlers[file_format](file_obj, **kwargs)
        self._loader.commit()
    finally:
        if isPath and file_obj is not None:
            file_obj.close()