def get_id(self, name, recurse=True):
    self._dlog("getting id '{}'".format(name))
    var = self._search('vars', name, recurse)
    return var