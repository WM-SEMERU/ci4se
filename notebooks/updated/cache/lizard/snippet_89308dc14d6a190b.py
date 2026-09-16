def _extract(self, path, outdir, filter_func=None):
    with open_zip(path) as archive_file:
        for name in archive_file.namelist():
            if name.startswith('/') or name.startswith('..'):
                raise ValueError('Zip file contains unsafe path: {}'.format
                    (name))
            if not filter_func or filter_func(name):
                archive_file.extract(name, outdir)