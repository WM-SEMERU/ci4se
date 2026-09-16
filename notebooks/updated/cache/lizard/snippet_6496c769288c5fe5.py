def load(self, value):
    self.reset(value, validator=self.__dict__.get('validator'), env=self.
        __dict__.get('env'))