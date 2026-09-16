def extend(self, assembly):
    if isinstance(assembly, Assembly):
        self._molecules.extend(assembly)
    else:
        raise TypeError('Only Assembly objects may be merged with an Assembly.'
            )
    return