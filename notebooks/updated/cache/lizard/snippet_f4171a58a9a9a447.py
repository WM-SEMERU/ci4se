def xatom(self, atom):
    handle = atom.handle
    if handle == self.atoms[0].handle:
        return self.atoms[1]
    elif handle == self.atoms[1].handle:
        return self.atoms[0]
    return None