def send(self, diff):
    if Store.skipDryRun(logger, self.dryrun)('send %s', diff):
        return None
    diffTo, diffFrom = self.toArg.diff(diff)
    self._client.send(diffTo, diffFrom)
    progress = DisplayProgress(diff.size
        ) if self.showProgress is True else None
    return _SSHStream(self._client, progress)