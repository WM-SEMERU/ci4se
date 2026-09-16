def report(self, name, owner=None, **kwargs):
    return Report(self.tcex, name, owner=owner, **kwargs)