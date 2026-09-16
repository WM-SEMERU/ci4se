def chown(self, paths, owner, recurse=False):
    if not isinstance(paths, list):
        raise InvalidInputException('Paths should be a list')
    if not paths:
        raise InvalidInputException('chown: no path given')
    if not owner:
        raise InvalidInputException('chown: no owner given')
    processor = lambda path, node, owner=owner: self._handle_chown(path,
        node, owner)
    for item in self._find_items(paths, processor, include_toplevel=True,
        include_children=False, recurse=recurse):
        if item:
            yield item