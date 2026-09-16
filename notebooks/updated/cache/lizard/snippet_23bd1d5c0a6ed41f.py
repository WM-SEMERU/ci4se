def create(self, name):
    vg = self.attach(-1, 1)
    vg._name = name
    return vg