def getEditorBinary(self, cmdVersion=False):
    return os.path.join(self.getEngineRoot(), 'Engine', 'Binaries', self.
        getPlatformIdentifier(), 'UE4Editor' + self._editorPathSuffix(
        cmdVersion))