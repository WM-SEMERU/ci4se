def package_url(self):
    return MetapackDocumentUrl(str(self.clear_fragment()), downloader=self.
        _downloader).package_url