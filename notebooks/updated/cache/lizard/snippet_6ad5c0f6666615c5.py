def parameter_names(self, add_self=False, adjust_for_printing=False,
    recursive=True, intermediate=False):
    if adjust_for_printing:
        adjust = adjust_name_for_printing
    else:
        adjust = lambda x: x
    names = []
    if intermediate or not recursive:
        names.extend([adjust(x.name) for x in self.parameters])
    if intermediate or recursive:
        names.extend([xi for x in self.parameters for xi in x.
            parameter_names(add_self=True, adjust_for_printing=
            adjust_for_printing, recursive=True, intermediate=False)])
    if add_self:
        names = map(lambda x: adjust(self.name) + '.' + x, names)
    return names