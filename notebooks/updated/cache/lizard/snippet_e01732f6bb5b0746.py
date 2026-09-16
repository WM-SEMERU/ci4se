def insertBefore(self, newchild, refchild):
    for i, childNode in enumerate(self.childNodes):
        if childNode is refchild:
            self.childNodes.insert(i, newchild)
            newchild.parentNode = self
            self._verifyChildren(i)
            return newchild
    raise ValueError(refchild)