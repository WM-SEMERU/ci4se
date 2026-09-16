def keep(self, diff):
    path = self.extraKeys[diff]
    if not path.startswith('/'):
        logger.debug('Keeping %s', path)
        del self.extraKeys[diff]
        return
    keyName = self._keyName(diff.toUUID, diff.fromUUID, path)
    newPath = os.path.join(self.userPath, os.path.basename(path))
    newName = self._keyName(diff.toUUID, diff.fromUUID, newPath)
    if not self._skipDryRun(logger)('Copy %s to %s', keyName, newName):
        self.bucket.copy_key(newName, self.bucket.name, keyName)