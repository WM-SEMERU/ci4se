def resume(self):
    with self.readSharedFileStream('config.pickle') as fileHandle:
        config = safeUnpickleFromStream(fileHandle)
        assert config.workflowID is not None
        self.__config = config