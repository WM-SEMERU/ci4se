def open_files(self, path):
    paths = []
    input_list = _patt.findall(path)
    if not input_list:
        input_list = [path]
    for path in input_list:
        if path.endswith('*'):
            path = path[:-1]
        if os.path.isdir(path):
            continue
        self.logger.debug('Opening files matched by {0}'.format(path))
        info = iohelper.get_fileinfo(path)
        ext = iohelper.get_hdu_suffix(info.numhdu)
        files = glob.glob(info.filepath)
        paths.extend(['{0}{1}'.format(f, ext) for f in files])
    if len(paths) > 0:
        self.load_paths(paths)
        return True
    return False