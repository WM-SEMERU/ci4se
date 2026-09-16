def parse_manifest(self, fpath):
    with open(fpath, 'r') as fh:
        for entry in json.load(fh):
            if 'filename' not in entry:
                raise RuntimeError('Entries in {} need to have "filename"'.
                    format(fpath))
            filename = entry.pop('filename')
            proxy_image = None
            if isinstance(self, MicroscopyCollection):
                proxy_image = MicroscopyImage(filename, entry)
            else:
                proxy_image = ProxyImage(filename, entry)
            self.append(proxy_image)