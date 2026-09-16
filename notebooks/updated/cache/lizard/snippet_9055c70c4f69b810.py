def _read_notebook(self, os_path, as_version=4):
    with self.open(os_path, 'r', encoding='utf-8') as f:
        try:
            file_ext = _file_extension(os_path)
            if file_ext == '.ipynb':
                return nbformat.read(f, as_version=as_version)
            else:
                return convert(os_path, from_=self.format, to='notebook')
        except Exception as e:
            raise HTTPError(400, 'Unreadable Notebook: %s %r' % (os_path, e))