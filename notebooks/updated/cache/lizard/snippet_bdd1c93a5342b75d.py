def load_xml(self, filepath):
    from os import path
    import xml.etree.ElementTree as ET
    uxpath = path.expanduser(filepath)
    if path.isfile(uxpath):
        tree = ET.parse(uxpath)
        root = tree.getroot()
        if 'symlink' in root.attrib:
            self._vardict['symlink'] = root.attrib.lower() == 'true'
        for child in root:
            if child.tag == 'codes':
                self._load_codes(child)
            elif child.tag == 'mappings':
                self._load_mapping(child)
            elif child.tag == 'ssh':
                self._load_ssh(child)
            elif child.tag == 'isense':
                self._load_isense(child)
            elif child.tag == 'libraries':
                self._load_includes(child)
            elif child.tag == 'compilers':
                self._vardict['compilers'] = child.text