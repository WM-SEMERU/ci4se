def startElement(self, node):
    if node is None:
        return
    if self.__filter_location is not None:
        if node.location.file is None:
            return
        elif node.location.file.name not in self.__filter_location:
            return
    log.debug('%s:%d: Found a %s|%s|%s', node.location.file, node.location.
        line, node.kind.name, node.displayname, node.spelling)
    try:
        stop_recurse = self.parse_cursor(node)
        if stop_recurse is not False:
            return
        for child in node.get_children():
            self.startElement(child)
    except InvalidDefinitionError:
        pass
    return None