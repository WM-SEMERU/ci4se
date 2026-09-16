def Detect(self, progs):
    if not SCons.Util.is_List(progs):
        progs = [progs]
    for prog in progs:
        path = self.WhereIs(prog)
        if path:
            return prog
    return None