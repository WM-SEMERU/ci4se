def load_doge(self):
    if self.ns.no_shibe:
        return ['']
    with open(self.doge_path) as f:
        if sys.version_info < (3, 0):
            if locale.getpreferredencoding() == 'UTF-8':
                doge_lines = [l.decode('utf-8') for l in f.xreadlines()]
            else:
                doge_lines = [l.decode('utf-8').encode(locale.
                    getpreferredencoding(), 'replace').replace('?', ' ') for
                    l in f.xreadlines()]
        else:
            doge_lines = [l for l in f.readlines()]
        return doge_lines