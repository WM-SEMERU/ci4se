def touchz(self, paths, replication=None, blocksize=None):
    if not isinstance(paths, list):
        raise InvalidInputException('Paths should be a list')
    if not paths:
        raise InvalidInputException('touchz: no path given')
    if not replication or not blocksize:
        defaults = self.serverdefaults()
    if not replication:
        replication = defaults['replication']
    if not blocksize:
        blocksize = defaults['blockSize']
    processor = (lambda path, node, replication=replication, blocksize=
        blocksize: self._handle_touchz(path, node, replication, blocksize))
    for item in self._find_items(paths, processor, include_toplevel=True,
        check_nonexistence=True, include_children=False):
        if item:
            yield item