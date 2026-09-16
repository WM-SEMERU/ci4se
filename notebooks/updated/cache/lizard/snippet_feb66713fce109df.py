def replaceChild(self, newchild, oldchild):
    for i, childNode in enumerate(self.childNodes):
        if childNode is oldchild:
            self.childNodes[i].parentNode = None
            self.childNodes[i] = newchild
            newchild.parentNode = self
            self._verifyChildren(i)
            return newchild
    raise ValueError(oldchild)