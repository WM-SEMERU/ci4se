def deleteUnused(self):
    if self.dryrun:
        self._client.listUnused()
    else:
        self._client.deleteUnused()