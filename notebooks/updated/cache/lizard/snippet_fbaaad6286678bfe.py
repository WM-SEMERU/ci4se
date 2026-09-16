def get_name(self, type_, id_):
    cachefile = self.filename(type_, id_)
    try:
        with open(cachefile, 'r') as f:
            return f.read()
    except (OSError, IOError) as e:
        if e.errno != errno.ENOENT:
            raise