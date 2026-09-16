def root(self):
    if not self.parent:
        return self
    con = self.parent
    while con.parent:
        con = con.parent
    return con