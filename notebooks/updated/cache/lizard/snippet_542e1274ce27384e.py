def create_information(self):
    info = self._info_type()(origin=self, contents=self._contents())
    return info