def qname(self):
    if self.parent is None:
        return self.name
    return '%s.%s' % (self.parent.frame().qname(), self.name)