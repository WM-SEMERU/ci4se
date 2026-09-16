def _open(self, name=None, fileobj=None, mymap=None, block=None):
    if block is not None:
        if not name:
            name = '<unknown>'
        self.unpack_from(block)
        if fileobj:
            fileobj.close()
        return self
    if mymap is not None:
        block = mymap
    elif fileobj:
        try:
            mymap = mmap.mmap(fileobj.fileno(), 0, mmap.MAP_SHARED, mmap.
                PROT_READ)
        except:
            mymap = 0
            block = fileobj.read()
    elif name:
        fileobj = io.open(os.path.normpath(os.path.expanduser(name)), 'rb')
    else:
        assert False
    return self._open(name=name, fileobj=fileobj, mymap=mymap, block=block)