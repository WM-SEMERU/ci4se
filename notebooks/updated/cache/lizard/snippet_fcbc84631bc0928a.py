def rename2(self, path, dst, overwriteDest=False):
    if not path:
        raise InvalidInputException('rename2: no path given')
    if not dst:
        raise InvalidInputException('rename2: no destination given')
    if not isinstance(path, (str, unicode)):
        raise InvalidInputException('rename2: Path should be a string')
    processor = (lambda path, node, dst=dst, overwriteDest=overwriteDest:
        self._handle_rename2(path, node, dst, overwriteDest))
    for item in self._find_items([path], processor, include_toplevel=True):
        return item