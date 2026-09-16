def aws(self):
    if self._aws is None:
        self._aws = AwsList(self._version)
    return self._aws