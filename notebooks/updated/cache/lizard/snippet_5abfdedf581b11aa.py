def endInstance(self):
    if self.currentInstance is None:
        return
    allInstances = self.root.findall('.instances')[0].append(self.
        currentInstance)
    self.currentInstance = None