def convert(self, vroot, entry_variables):
    for converter in self.converters:
        vroot = converter.convert(vroot, entry_variables)
    return vroot