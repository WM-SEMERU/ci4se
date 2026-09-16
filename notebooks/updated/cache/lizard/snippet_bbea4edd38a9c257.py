def send(self, diffTo, diffFrom):
    diff = self.toObj.diff(diffTo, diffFrom)
    self._open(self.butterStore.send(diff))