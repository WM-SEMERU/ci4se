def _load_ssh(self, tag):
    for child in tag:
        if child.tag == 'server':
            self._vardict['server'] = child.attrib
        elif child.tag == 'codes':
            self._load_codes(child, True)
        elif child.tag == 'mappings':
            self._load_mapping(child, True)
        elif child.tag == 'libraries':
            self._load_includes(child, True)