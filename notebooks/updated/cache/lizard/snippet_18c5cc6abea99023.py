def running(self, aProcess, aThread):
    if self.__state != self.ENABLED:
        self.__bad_transition(self.RUNNING)
    self.__state = self.RUNNING