def mktns(self):
    tns = [None, self.root.get('targetNamespace')]
    if tns[1] is not None:
        tns[0] = self.root.findPrefix(tns[1])
    return tuple(tns)