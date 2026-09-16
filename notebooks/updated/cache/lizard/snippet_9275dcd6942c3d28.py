def globalize(self):
    try:
        with open(os.path.join(self.dirPath, '.stash')) as f:
            fromVirtualEnv = [False, True][int(f.read(1))]
            dirPath = f.read()
    except IOError as e:
        if e.errno == errno.ENOENT:
            if self._runningOnWorker():
                log.warn("Can't globalize module %r.", self)
            return self
        else:
            raise
    else:
        return self.__class__(dirPath=dirPath, name=self.name,
            fromVirtualEnv=fromVirtualEnv)