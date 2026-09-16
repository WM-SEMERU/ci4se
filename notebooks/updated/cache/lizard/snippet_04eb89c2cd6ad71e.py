def download_slides(self):
    return self.presentation.client.download_all(self.presentation.metadata
        ['slides'], self.tmp_dir)