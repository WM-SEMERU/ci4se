def get_files(self, is_dl_forced, files=None):
    fstat = None
    if files is None:
        files = self.files
    for fname in files:
        LOG.info('Getting %s', fname)
        headers = None
        filesource = files[fname]
        if 'headers' in filesource:
            headers = filesource['headers']
        self.fetch_from_url(filesource['url'], '/'.join((self.rawdir,
            filesource['file'])), is_dl_forced, headers)
        if 'clean' in filesource and filesource['clean'] is not None:
            self.dataset.setFileAccessUrl(filesource['clean'])
        else:
            self.dataset.setFileAccessUrl(filesource['url'])
        fstat = os.stat('/'.join((self.rawdir, filesource['file'])))
    filedate = datetime.utcfromtimestamp(fstat[ST_CTIME]).strftime('%Y-%m-%d')
    self.dataset.set_date_issued(filedate)