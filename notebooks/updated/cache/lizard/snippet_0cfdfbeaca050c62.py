def from_names(cls, *names):
    new = cls()
    for namestr in names:
        for name in cls._split_names(namestr):
            new.append(Channel(name))
    return new