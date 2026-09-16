def __callbackWrapper(self, transfer_p):
    self.__submitted = False
    self.__after_completion(self)
    callback = self.__callback
    if callback is not None:
        callback(self)
    if self.__doomed:
        self.close()