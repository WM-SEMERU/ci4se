def newchild(self, chld=False):
    if not chld:
        chld = self.givebirth()
    lchld = [chld] if type(chld) != list else chld
    for chldx in lchld:
        chldx.parent = self
    self.children.append(chld)
    return chld