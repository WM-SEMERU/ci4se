def emitFileTriggered(self, action):
    if not self.signalsBlocked():
        filename = nativestring(unwrapVariant(action.data()))
        self.fileTriggered.emit(filename)