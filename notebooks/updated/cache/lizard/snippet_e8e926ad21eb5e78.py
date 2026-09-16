def submodules(self):
    submodules = []
    submodules.extend(self.modules)
    for p in self.packages:
        submodules.extend(p.submodules)
    return submodules