def delete(self, paths, recurse=False):
    if not isinstance(paths, list):
        raise InvalidInputException('Paths should be a list')
    if not paths:
        raise InvalidInputException('delete: no path given')
    processor = lambda path, node, recurse=recurse: self._handle_delete(path,
        node, recurse)
    for item in self._find_items(paths, processor, include_toplevel=True):
        if item:
            yield item