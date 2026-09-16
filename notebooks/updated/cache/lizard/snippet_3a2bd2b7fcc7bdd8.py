def build(self):
    self.children = BasicFactory.build(self.root, self)
    collated = BasicFactory.collate(self.children)
    self.children = collated[0]
    self.attributes = collated[2]
    self.imports = collated[1]
    self.elements = collated[3]
    self.types = collated[4]
    self.groups = collated[5]
    self.agrps = collated[6]