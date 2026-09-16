def tube(self, name):
    tube = self.tubes.get(name)
    if tube is None:
        tube = Tube(self, name)
        self.tubes[name] = tube
    return tube