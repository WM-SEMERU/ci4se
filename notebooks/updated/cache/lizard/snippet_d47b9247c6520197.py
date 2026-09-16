def load(self, filename):
    self.tree = xmltreefromfile(filename)
    self.parsexml(self.tree.getroot())
    if self.mode != Mode.XPATH:
        self.tree = None