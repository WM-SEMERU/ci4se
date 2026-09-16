def create(self, data, *args, **kwargs):
    if self.create.__func__.__module__ != self.__module__:
        raise Exception('Child method not implemented')
    self._MambuStruct__method = 'POST'
    self._MambuStruct__data = data
    self.connect(*args, **kwargs)
    self._MambuStruct__method = 'GET'
    self._MambuStruct__data = None