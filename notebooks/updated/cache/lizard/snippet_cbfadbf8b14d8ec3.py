def export(self, name):
    self.name = name
    root = self._create_doc()
    self._set_description(root)
    self._set_preferences(root)
    self._set_repositories(root)
    self._set_users(root)
    self._set_packages(root)
    return '\n'.join([line for line in minidom.parseString(etree.tostring(
        root, encoding='UTF-8', pretty_print=True)).toprettyxml(indent='  '
        ).split('\n') if line.strip()])