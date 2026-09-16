def directory_create(self, path, mode, flags):
    if not isinstance(path, basestring):
        raise TypeError('path can only be an instance of type basestring')
    if not isinstance(mode, baseinteger):
        raise TypeError('mode can only be an instance of type baseinteger')
    if not isinstance(flags, list):
        raise TypeError('flags can only be an instance of type list')
    for a in flags[:10]:
        if not isinstance(a, DirectoryCreateFlag):
            raise TypeError(
                'array can only contain objects of type DirectoryCreateFlag')
    self._call('directoryCreate', in_p=[path, mode, flags])