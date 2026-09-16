def get(self):
    value = {}
    for elementname, elementvar in self._elementvars.items():
        value[elementname] = elementvar.get()
    return value