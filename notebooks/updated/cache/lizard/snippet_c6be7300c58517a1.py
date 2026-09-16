def get(self):
    self.log.debug('starting the ``get`` method')
    if self.format == 'epub':
        if self.urlOrPath[:4] == 'http' or self.urlOrPath[:4] == 'www.':
            ebook = self._url_to_epub()
        elif '.docx' in self.urlOrPath:
            ebook = self._docx_to_epub()
    if self.format == 'mobi':
        if self.urlOrPath[:4] == 'http' or self.urlOrPath[:4] == 'www.':
            epub = self._url_to_epub()
        elif '.docx' in self.urlOrPath:
            epub = self._docx_to_epub()
        if not epub:
            return None
        ebook = self._epub_to_mobi(epubPath=epub, deleteEpub=False)
    tag(log=self.log, filepath=ebook, tags=False, rating=False, wherefrom=
        self.url)
    self.log.debug('completed the ``get`` method')
    return ebook