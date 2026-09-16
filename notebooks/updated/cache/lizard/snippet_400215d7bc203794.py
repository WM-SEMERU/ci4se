def compact(self):
    self.docFactory = webtheme.getLoader(self.compactFragmentName)
    for param in self.parameters:
        param.compact()