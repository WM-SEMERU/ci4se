def check_connection(self):
    if self.parent_url is not None and not self.parent_url.startswith('file:'):
        msg = _(
            'local files are only checked without parent URL or when the parent URL is also a file'
            )
        raise LinkCheckerError(msg)
    if self.is_directory():
        self.set_result(_('directory'))
    else:
        url = fileutil.pathencode(self.url)
        self.url_connection = urlopen(url)
        self.check_case_sensitivity()