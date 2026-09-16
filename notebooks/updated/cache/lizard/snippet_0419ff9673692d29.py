def uniquetwig(self, ps=None):
    if ps is None:
        ps = self._bundle
    if ps is None:
        return self.twig
    return ps._uniquetwig(self.twig)