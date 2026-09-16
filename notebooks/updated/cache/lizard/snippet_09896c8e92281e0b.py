def purge(self, ignore_ignores):
    command = ['status', '--xml']
    if ignore_ignores:
        command.append('--no-ignore')
    d = self._dovccmd(command, collectStdout=True)

    @d.addCallback
    def parseAndRemove(stdout):
        files = []
        for filename in self.getUnversionedFiles(stdout, self.keep_on_purge):
            filename = self.build.path_module.join(self.workdir, filename)
            files.append(filename)
        if not files:
            d = defer.succeed(0)
        elif self.workerVersionIsOlderThan('rmdir', '2.14'):
            d = self.removeFiles(files)
        else:
            d = self.runRmdir(files, abandonOnFailure=False, timeout=self.
                timeout)
        return d

    @d.addCallback
    def evaluateCommand(rc):
        if rc != 0:
            log.msg('Failed removing files')
            raise buildstep.BuildStepFailed()
        return rc
    return d