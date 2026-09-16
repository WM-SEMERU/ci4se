def packto(self, namedstruct, stream):
    if hasattr(namedstruct, self.name):
        return _tostream(self.basetypeparser, getattr(namedstruct, self.
            name), stream, True)
    else:
        return 0