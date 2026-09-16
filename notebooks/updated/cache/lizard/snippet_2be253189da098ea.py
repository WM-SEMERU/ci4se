def scan_models(self, folder='./yang', download='check'):
    d = ModelDownloader(self, folder)
    if download == 'force':
        d.download_all(check_before_download=False)
    elif download == 'check':
        d.download_all(check_before_download=True)
    self.compiler = ModelCompiler(folder)