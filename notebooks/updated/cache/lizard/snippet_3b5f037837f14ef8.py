def getindex(self, child, recursive=True, ignore=True):
    for i, c in enumerate(self.data):
        if c is child:
            return i
    if recursive:
        for i, c in enumerate(self.data):
            if ignore is True:
                try:
                    if not c.auth:
                        continue
                except AttributeError:
                    pass
            elif ignore:
                doignore = False
                for e in ignore:
                    if e is True:
                        try:
                            if not c.auth:
                                doignore = True
                                break
                        except AttributeError:
                            pass
                    elif e == c.__class__ or issubclass(c.__class__, e):
                        doignore = True
                        break
                if doignore:
                    continue
            if isinstance(c, AbstractElement):
                j = c.getindex(child, recursive)
                if j != -1:
                    return i
    return -1