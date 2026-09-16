def save(self, filename):
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    projex.text.xmlindent(self._xroot)
    xtree = ElementTree.ElementTree(self._xroot)
    xtree.write(filename, encoding=self.encoding(), xml_declaration=True)
    return True