def closest(self, tag):
    return CSSMatch(self.selectors, tag, self.namespaces, self.flags).closest()