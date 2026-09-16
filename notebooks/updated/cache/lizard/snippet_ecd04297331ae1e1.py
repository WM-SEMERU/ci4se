def fetch(self):
    if not self.local_path:
        self.make_local_path()
    fetcher = BookFetcher(self)
    fetcher.fetch()