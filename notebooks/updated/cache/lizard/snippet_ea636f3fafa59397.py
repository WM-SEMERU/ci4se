def _parse_tree(self, node):
    self.kind = node.tag
    if 'compare' in node.attrib:
        self.compare = node.attrib['compare']
    if 'version' in node.attrib:
        self.version = node.attrib['version']
    self.value = node.text