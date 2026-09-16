def filedata(self):
    if self._filedata_api is None:
        self._filedata_api = self.get_filedata_api()
    return self._filedata_api