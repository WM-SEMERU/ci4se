def parse(self, root):
    v = _get_xml_version(root)[0]
    result = {}
    for child in root:
        if child.tag in self.versions[v].entries:
            entry = self.versions[v].entries[child.tag]
            result[child.tag] = entry.parse(child)
    return result