def add_size_info(self):
    maxbytes = self.aggregate.config['maxfilesizedownload']
    if self.size > maxbytes:
        self.add_warning(_(
            'Content size %(size)s is larger than %(maxbytes)s.') % dict(
            size=strformat.strsize(self.size), maxbytes=strformat.strsize(
            maxbytes)), tag=WARN_URL_CONTENT_SIZE_TOO_LARGE)